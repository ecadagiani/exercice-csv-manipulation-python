from abc import ABC, abstractmethod
import csv
from pathlib import Path

class CsvModel(ABC):
    instances = []
    is_loaded = False
    file_path = None
    
    @classmethod
    @abstractmethod
    def create_instance_from_row(cls, row):
        """
        Abstract method to create an instance from a CSV row
        Args:
            row: Dictionary containing the CSV row data
        Returns:
            Instance of the child class
        """
        pass
    
    @classmethod
    @abstractmethod
    def to_row(cls, instance):
        """
        Abstract method to convert an instance to a CSV row
        Args:
            instance: Instance to convert
        Returns:
            Dictionary representing the CSV row
        """
        pass
    
    @classmethod
    def get(cls, id_value):
        """
        Retrieve an instance by its ID. Loads data if not already loaded.
        Args:
            id_value: The ID to find
        Returns:
            Instance of the class or None
        """
        if not cls.is_loaded:
            cls.load()
            
        id_str = int(id_value)
        for instance in cls.instances:
            # We assume each class has an ID field ending with '_id'
            if getattr(instance, "id") == id_str:
                return instance
        return None
    
    @classmethod
    def load(cls):
        """
        Load all instances from the CSV file
        Returns:
            list: List of instances
        """
        if not cls.file_path:
            raise ValueError(f"file_path not set for {cls.__name__}")
            
        if cls.is_loaded:
            return cls.instances
        
        cls.instances = []
        with open(cls.file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                instance = cls.create_instance_from_row(row)
                cls.instances.append(instance)
        
        cls.is_loaded = True
        return cls.instances
    
    @classmethod
    def save(cls):
        """
        Save all instances back to the CSV file
        """
        if not cls.file_path:
            raise ValueError(f"file_path not set for {cls.__name__}")
            
        with open(cls.file_path, 'w', newline='') as file:
            # Get fieldnames from the first instance or from the child class
            if cls.instances:
                first_row = cls.to_row(cls.instances[0])
                fieldnames = list(first_row.keys())
            else:
                raise ValueError(f"No instances to save for {cls.__name__}")
                
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for instance in cls.instances:
                writer.writerow(cls.to_row(instance))

    @classmethod
    def get_next_available_id(cls):
        """
        Get the next available ID for a new instance
        Returns:
            str: Next available ID
        """
        if not cls.instances:
            return 1
            
        # Get all existing IDs and find the maximum
        existing_ids = []
        for instance in cls.instances:
            existing_ids.append(int(instance.id)) # Verify to convert to int to avoid string comparison issues
        return max(existing_ids) + 1
