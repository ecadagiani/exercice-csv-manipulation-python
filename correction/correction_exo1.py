
import os

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

files = get_file_names('data')
csv_files = get_csv_files('data')

print(f"Fichiers csv trouvés : {csv_files}")

while True:
    file_name = input("Entrez le nom du fichier (sans extension) : ")

    matching_files = find_matching_files(files, file_name)
    
    if matching_files:
        if len(matching_files) == 1:
            print(f"Le fichier {matching_files[0]} existe")
        else:
            print("Plusieurs fichiers trouvés :")
            for f in matching_files:
                print(f"- {f}")
        break
    else:
        print("Le fichier n'existe pas")