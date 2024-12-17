from .CsvModel import CsvModel
from pathlib import Path
from .User import User
from .Product import Product
from .Invoice import Invoice
from datetime import datetime
class Order(CsvModel):
    file_path = Path('data/orders.csv')
    
    def __init__(self, user, product, quantity, invoice):
        """
        Initialize an Order instance
        Args:
            user: User instance who placed the order
            product: Product instance that was ordered
            quantity: Quantity ordered
            invoice: Invoice instance associated with this order
        """
        self.user = user
        self.product = product
        self.quantity = int(quantity)
        self.invoice = invoice
    
    @classmethod
    def create_instance_from_row(cls, row):
        """
        Create an Order instance from a CSV row
        Args:
            row: Dictionary containing the CSV row data
        Returns:
            Order: New Order instance
        """
        # Get related instances using their respective get methods
        user = User.get(row['user_id'])
        product = Product.get(row['product_id'])
        invoice = Invoice.get(row['invoice_id'])
        
        # Verify that all related instances exist
        if not user:
            raise ValueError(f"User {row['user_id']} not found")
        if not product:
            raise ValueError(f"Product {row['product_id']} not found")
        if not invoice:
            raise ValueError(f"Invoice {row['invoice_id']} not found")
            
        return cls(
            user=user,
            product=product,
            quantity=row['quantity'],
            invoice=invoice
        )
    
    @classmethod
    def to_row(cls, instance):
        """
        Convert an Order instance to a CSV row
        Args:
            instance: Order instance to convert
        Returns:
            dict: Dictionary representing the CSV row
        """
        return {
            'user_id': instance.user.id,
            'product_id': instance.product.id,
            'quantity': instance.quantity,
            'invoice_id': instance.invoice.id
        }
    
    @classmethod
    def load(cls):
        """
        Override load method to ensure dependent data is loaded first
        Returns:
            list: List of Order instances
        """
        if Order.is_loaded:
            return Order.instances
        
        # Load all required data first
        User.load()
        Product.load()
        Invoice.load()
        
        # Then load orders
        return super().load()
    
    def get_total_price(self):
        """
        Calculate the total price for this order line
        Returns:
            float: Total price (quantity * unit price)
        """
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"Order(user={self.user.id}, product={self.product.id}, quantity={self.quantity}, invoice={self.invoice.id})"

    @classmethod
    def command_create_orders(cls):
      """
      Create a new invoice with multiple order lines.
      Asks for user, payment method, and then loops for products until done.
      """
      print("\n=== Creating New Invoice ===")
      
      # Get user
      while True:
          user_id = input("Enter user ID: ")
          user = User.get(user_id)
          if user:
              break
          print(f"User {user_id} not found. Please try again.")
      
      # Get payment method
      valid_methods = ['CARD', 'PAYPAL', 'BANK_TRANSFER']
      while True:
          print("\nAvailable payment methods:", ', '.join(valid_methods))
          payment_method = input("Enter payment method: ").upper()
          if payment_method in valid_methods:
              break
          print("Invalid payment method. Please try again.")
      
      # Create new invoice with 0 total (will be calculated later)
      new_invoice = Invoice(
          id=Invoice.get_next_available_id(),
          total_price=0,
          datetime_str=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
          payment_method=payment_method
      )

      # List to store order lines
      orders = []
      total_price = 0
      
      # Loop for asking products
      while True:
          print("\n=== Add Product to Invoice ===")
          print("(Press Enter without product ID to finish)")
          
          # Get product
          product_id = input("Enter product ID: ")
          if not product_id:  # Empty input means we're done
              break
              
          product = Product.get(product_id)
          if not product:
              print(f"Product {product_id} not found.")
              continue
              
          if product.archived:
              print(f"Product {product.name} is archived and cannot be ordered.")
              continue
          
          # Get quantity
          while True:
              try:
                  quantity = int(input(f"Enter quantity (available: {product.quantity}): "))
                  # int() will raise an error if the input is not a valid integer
                  if quantity <= 0:
                      print("Quantity must be positive.")
                  elif quantity > product.quantity:
                      print(f"Not enough stock. Only {product.quantity} available.")
                  else:
                      break
              except ValueError:
                  print("Please enter a valid number.")
          
          # Create order
          order = Order(
              user=user,
              product=product,
              quantity=quantity,
              invoice=new_invoice
          )
          
          # Update product quantity
          product.quantity -= quantity
          
          # Add to orders list and update total
          orders.append(order)
          total_price += order.get_total_price()
          
          # Show current total
          print(f"\nCurrent total: ${total_price:.2f}")
      
      # If no orders were created, abort
      if not orders:
          print("No products selected. Invoice creation cancelled.")
          return
      
      # Update invoice total
      new_invoice.total_price = total_price
      
      # Save all in instances
      Invoice.instances.append(new_invoice)
      Order.instances.extend(orders)

      # Remove product from stock
      for order in orders:
          order.product.remove_from_stock(order.quantity)
      
      # Show summary
      print("\n=== Invoice Summary ===")
      print(f"Invoice ID: {new_invoice.id}")
      print(f"Customer: {user.firstname} {user.lastname}")
      print(f"Payment Method: {new_invoice.payment_method}")
      print("\nOrdered Products:")
      for order in orders:
          print(f"- {order.product.name} x{order.quantity}: ${order.get_total_price():.2f}")
      print(f"\nTotal Amount: ${total_price:.2f}")