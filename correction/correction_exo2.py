import os
import csv


def get_file_names(folder_path):
    return os.listdir(folder_path)

def find_matching_files(files, name):
    matches = []
    for f in files:
        if f.split('.')[0] == name:
            matches.append(f)
    return matches

def get_csv_files(folder_path):
    csv_files = []
    files = get_file_names(folder_path)
    for f in files:
        if f.endswith('.csv'):
            csv_files.append(f)
    return csv_files

def get_headers(first_line, separator):
    headers = first_line.split(separator)
    # -1 allows you to retrieve the last element of the array, it's the same that `headers[len(headers) - 1]``
    headers[-1] = headers[-1].replace('\n', '')
    return headers

def create_simple_table(lines, separator):
    table = []
    for line in lines:
        parsed_line = line.replace('\n', '')
        table.append(parsed_line.split(separator))
    return table

def create_dict_table(lines, separator, headers):
    table = []
    for line in lines:
        parsed_line = line.replace('\n', '')
        line_dict = {}
        for i, header in enumerate(headers):
            line_dict[header] = parsed_line.split(separator)[i]
        table.append(line_dict)
    return table

def create_dict_table_csv(file, separator):
    table = csv.DictReader(file, delimiter=separator)
    return table



csv_files = get_csv_files('data')

print(f"Fichiers csv disponibles : {csv_files}")

while True:
    file_name = input("Entrez le nom du fichier csv (sans extension) : ")

    matching_files = find_matching_files(csv_files, file_name)
    
    if not matching_files:
        print("Le fichier n'existe pas")
    elif len(matching_files) > 1:
        raise ValueError("Multiple csv files found")
    else:
        filename = matching_files[0]
        with open(f"data/{filename}", "r") as f:
            # lines = f.readlines()
            # print(f"Le fichier {filename} contient {len(lines)} lignes")
            # headers = get_headers(lines[0], ',')
            # print(f"Les entêtes du fichier sont : {headers}")
            # table = create_simple_table(lines, ',')
            # table = create_dict_table(lines, ',', headers)

            table = create_dict_table_csv(f, ',')
            print(list(table))
        break
