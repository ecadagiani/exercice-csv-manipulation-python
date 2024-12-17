from .CsvModel import CsvModel
from pathlib import Path
from datetime import datetime

class User(CsvModel):
    file_path = Path('data/users.csv')
    
    def __init__(self, id, lastname, firstname, email, creation_date, language, country):
        self.id = int(id)
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.creation_date = datetime.strptime(creation_date, '%Y-%m-%d').date()
        self.language = language
        self.country = country
    
    @classmethod
    def create_instance_from_row(cls, row):
        return cls(
            id=row['user_id'],
            lastname=row['lastname'],
            firstname=row['firstname'],
            email=row['email'],
            creation_date=row['creation_date'],
            language=row['language'],
            country=row['country']
        )
    
    @classmethod
    def to_row(cls, instance):
        return {
            'user_id': instance.id,
            'lastname': instance.lastname,
            'firstname': instance.firstname,
            'email': instance.email,
            'creation_date': instance.creation_date,
            'language': instance.language,
            'country': instance.country
        }
    
    @classmethod
    def command_create_user(cls):
        lastname = input("Enter the user's last name: ")
        firstname = input("Enter the user's first name: ")
        email = input("Enter the user's email: ")
        creation_date = input("Enter the user's creation date (YYYY-MM-DD): ")
        language = input("Enter the user's language (FR, EN, US, ES, DE, IT): ")
        country = input("Enter the user's country (FR, EN, US, ES, DE, IT): ")
        id = cls.get_next_available_id()
        user = User(
            id=id,
            lastname=lastname,
            firstname=firstname,
            email=email,
            creation_date=creation_date,
            language=language,
            country=country
        )
        cls.instances.append(user)
        print(f"User created: {user}")
        return user
    
    def __str__(self):
        return f"User(id={self.id}, lastname={self.lastname}, firstname={self.firstname}, email={self.email}, creation_date={self.creation_date}, language={self.language}, country={self.country})"
