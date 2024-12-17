import csv

def read_csv_as_dict(filename):
    """
    Read a CSV file and return its contents as a list of dictionaries.
    Each row becomes a dictionary where column names are the keys.
    """
    with open(f'data/{filename}', 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def get_invoice_price(invoice_id, invoices):
    # find the invoice with the given invoice_id
    # recover invoices to avoid to read the csv each time
    for invoice in invoices:
        if invoice['invoice_id'] == invoice_id:
            return float(invoice['total_price'])
    raise ValueError(f"Invoice {invoice_id} not found")

def calculate_user_totals():
    """
    Calculate total spending for each user by combining invoice totals
    with invoice-user relationships.
    Returns a sorted list of tuples [(user_id, total_amount)] in descending order.
    """
    # Read orders
    orders = read_csv_as_dict('orders.csv')
    invoices = read_csv_as_dict('invoices.csv')
    
    # Initialize dictionary to store user totals
    user_totals = {}
    
    # Calculate total spending for each user
    for order in orders:
        user_id = order['user_id']
        invoice_id = order['invoice_id']
        
        invoice_price = get_invoice_price(invoice_id, invoices)
            
        # Add invoice amount to user's total
        if user_id in user_totals:
            user_totals[user_id] += invoice_price
        else:
            user_totals[user_id] = invoice_price
    
    # Convert to list of tuples 
    user_totals_list = user_totals.items() # [(user_id, total), ...]
    # sort by amount
    return sorted(user_totals_list, key=lambda x: x[1], reverse=True) # filter on second element

def get_top_customers(count=3):
    """
    Print the top customers (by default top 3) with their names, emails,
    and total spending.
    """
    # Get sorted user totals
    user_totals = calculate_user_totals()
    
    # Get user details from users.csv
    users = read_csv_as_dict('users.csv')
    
    # Create dictionary for quick user lookup
    user_dict = {}
    for user in users:
        user_dict[user['user_id']] = user
    
    print(f"\nTop {count} Customers:")
    print("-" * 50)
    
    # enumerate(user_totals) allows you to loop on item and index
    for i, (user_id, total) in enumerate(user_totals):
        # i+1 because enumerate starts at 0
        # break if we have reached the count
        if(i+1 > count):
            break
        
        # Print details for each top spender
        user = user_dict[user_id]
        print(f"{i+1}. Name: {user.get('lastname', 'Unknown')} {user.get('firstname', 'Unknown')}")
        print(f"   Email: {user.get('email', 'Unknown')}")
        print(f"   Total Spending: ${total:.2f}")
        print("-" * 50)

if __name__ == "__main__":
    get_top_customers(3)
