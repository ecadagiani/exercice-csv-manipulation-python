from .CsvModel import CsvModel
from pathlib import Path

class Product(CsvModel):
    file_path = Path('data/products.csv')
    
    def __init__(self, id, name, price, quantity, archived):
        self.id = int(id)
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.archived = archived.upper() in ['VRAI', 'TRUE', 'VRAIE', 'T', 'V']
    
    @classmethod
    def create_instance_from_row(cls, row):
        return cls(
            id=row['product_id'],
            name=row['name'],
            price=row['price'],
            quantity=row['quantity'],
            archived=row['archived']
        )
    
    @classmethod
    def to_row(cls, instance):
        return {
            'product_id': instance.id,
            'name': instance.name,
            'price': instance.price,
            'quantity': instance.quantity,
            'archived': 'VRAI' if instance.archived else 'FAUX'
        }


    @classmethod
    def command_create_product(cls):
        name = input("Enter the product's name: ")
        price = input("Enter the product's price: ")
        quantity = input("Enter the product's quantity: ")
        archived = input("Enter the product's archived status (VRAI, FAUX): ")
        id = cls.get_next_available_id()
        product = Product(
            id=id,
            name=name,
            price=price,
            quantity=quantity,
            archived=archived
        )
        cls.instances.append(product)

        print(f"Product created: {product}")
        return product

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity}, archived={self.archived})"
