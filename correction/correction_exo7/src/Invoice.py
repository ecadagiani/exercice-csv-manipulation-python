from .CsvModel import CsvModel
from pathlib import Path
from datetime import datetime

class Invoice(CsvModel):
    file_path = Path('data/invoices.csv')
    
    def __init__(self, id, total_price, datetime_str, payment_method):
        """
        Initialize an Invoice instance
        Args:
            id: Unique identifier for the invoice
            total_price: Total amount of the invoice
            datetime_str: Date and time of the invoice
            payment_method: Method of payment (CARD, PAYPAL, BANK_TRANSFER)
        """
        self.id = int(id)
        self.total_price = float(total_price)
        # Convert string to datetime object for easier manipulation
        self.datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        self.payment_method = payment_method
    
    @classmethod
    def create_instance_from_row(cls, row):
        """
        Create an Invoice instance from a CSV row
        Args:
            row: Dictionary containing the CSV row data
        Returns:
            Invoice: New Invoice instance
        """
        return cls(
            id=row['invoice_id'],
            total_price=row['total_price'],
            datetime_str=row['datetime'],
            payment_method=row['payment_method']
        )
    
    @classmethod
    def to_row(cls, instance):
        """
        Convert an Invoice instance to a CSV row
        Args:
            instance: Invoice instance to convert
        Returns:
            dict: Dictionary representing the CSV row
        """
        return {
            'invoice_id': instance.id,
            'total_price': instance.total_price,
            'datetime': instance.datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'payment_method': instance.payment_method
        } 

    def __str__(self):
        return f"Invoice(id={self.id}, total_price={self.total_price}, datetime={self.datetime}, payment_method={self.payment_method})"
