import csv

def get_currency_for_country(country):
    """
    Returns the appropriate currency code based on the country code.
    
    Args:
        country (str): Two-letter country code (FR, ES, US, UK)
    
    Returns:
        str: The corresponding currency code (EUR, USD, GBP)
    """
    # Dictionary mapping currencies to their countries
    currency_map = {
        'EUR': ['FR', 'ES'],
        'USD': ['US'],
        'GBP': ['UK']
    }
    
    # Find the currency where the country is in its list of countries
    for currency, countries in currency_map.items():
        if country in countries:
            return currency
    return None

def add_currency_to_users():
    """
    Reads the users.csv file, adds a currency column based on the country,
    and writes the result to a new file in the parsed_data directory.
    """
    # Open both input and output files
    # Using newline='' to prevent extra blank lines in the output
    with open('data/users.csv', 'r') as input_file, \
         open('parsed_data/users_with_currency.csv', 'w', newline='') as output_file:
        
        # Create a CSV reader that reads the input as dictionaries
        reader = csv.DictReader(input_file)
        
        # Get the existing fieldnames and add our new 'currency' field
        fieldnames = list(reader.fieldnames)
        fieldnames.append('currency')
        
        # Create a CSV writer with the updated fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        
        # Write the header row with the new currency column
        writer.writeheader()
        
        # Process each row in the input file
        for row in reader:
            # Get the currency based on the country code
            currency = get_currency_for_country(row['country'])
            
            # Add the currency to the row dictionary
            row['currency'] = currency if currency else 'UNKNOWN'
            
            # Write the modified row to the output file
            writer.writerow(row)

if __name__ == "__main__":
    add_currency_to_users()
