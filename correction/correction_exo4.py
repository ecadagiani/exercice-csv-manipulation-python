import csv

def convert_products_file():
    # Open two files simultaneously using a with statement:
    # - Source file in read mode ('r')
    # - Destination file in write mode ('w')
    # newline='' prevents extra blank lines between each data row
    with open('data/products.csv', 'r') as input_file, \
         open('parsed_data/products.csv', 'w', newline='') as output_file:
        
        # DictReader creates an object that reads the CSV file as a list of dictionaries
        # Each row becomes a dictionary where column names are the keys
        # Example: {'product_id': '1', 'name': 'Smartphone XS', 'price': '599.99', ...}
        reader = csv.DictReader(input_file)
        
        # DictWriter creates an object to write dictionaries to the CSV file
        # fieldnames parameter specifies the order of columns
        # We use the same column names as the source file (reader.fieldnames)
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames)
        
        # Write the header row to the new file
        # This creates the first line with column names
        writer.writeheader()
        
        # Process each row in the source file
        for row in reader:
            # Check if the 'archived' column exists in the current row
            if 'archived' in row:
                # Convert French 'VRAI' to English 'TRUE'
                if row['archived'] == 'VRAI':
                    row['archived'] = 'TRUE'
                # Convert French 'FAUX' to English 'FALSE'
                elif row['archived'] == 'FAUX':
                    row['archived'] = 'FALSE'
            
            # Write the modified row to the destination file
            # All other columns remain unchanged
            writer.writerow(row)

# This condition checks if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Call the conversion function when the script is run
    convert_products_file()
