import os
import csv
def write_hello_world_file():
    with open('parsed_data/test.txt', 'w') as f:
        f.write('Hello World')

users = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]

def write_users_csv_file():
    # Open the users.csv file in write mode ('w')
    # This will create a new file or overwrite an existing one
    with open('parsed_data/users.csv', 'w') as f:
        # Get the column headers from the keys of the first user dictionary
        # Convert to list so we can join them later
        headers_list = list(users[0].keys())
        
        # Write the headers as a comma-separated line
        # Join the headers with commas and add a newline at the end
        f.write(','.join(headers_list) + '\n')
        
        # Iterate through each user dictionary to write the data rows
        for user in users:
            # Create an empty list to store the values for this user
            user_value = []
            
            # For each header/column, get the corresponding value from the user dict
            # Make sure to convert all values to strings since we're writing text
            for header in headers_list:
                user_value.append(str(user[header]))
                
            # Join the user's values with commas and write as a new line
            # This maintains the same order as the headers
            f.write(','.join(user_value) + '\n')


def write_users_csv_file_with_csv_module():
    with open('parsed_data/users.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys())
        writer.writeheader()
        writer.writerows(users)


write_users_csv_file_with_csv_module()