# Python Exercise - CSV File Manipulation

> These exercises are designed for an audience discovering Python, but who have already learned the basics of the language through various courses. They will help put these skills into practice and consolidate their knowledge.

You will find CSV files in the `/data` folder.
Throughout the different exercises, you will be led to manipulate these files.
For simplicity, you will find a `main.py` file to complete the exercises. As you progress through the exercises, you will be asked to create your own files and folders.

## Exercise 1 - File Manipulation

### Function Call and Display
Here's the Python code to retrieve an array with all filenames in a given folder:

```python
import os

def get_file_names(folder_path):
    return os.listdir(folder_path)
```

Copy this function into the `main.py` file and call the function with the `/data` folder. Display the result.

<details>
<summary>Help</summary>

```python
files = get_file_names('data')
```
</details>

### Verify File Existence

1. At the beginning of the program, ask the user to enter a filename. Check if the file exists in the `/data` folder. If the file does not exist, display an error message and ask the user to enter a new filename.
2. It is tedious for the user to have to enter the file extension. Modify the code so that the user only enters the filename. If multiple files exist with the same name, display all existing files.

<details>
<summary>Help</summary>

To retrieve the list of files with the given name:

1. Use a `for` loop to iterate through the list of files.
2. Split the filename to retrieve its name without the extension using `.split()`. (https://docs.python.org/3.3/library/stdtypes.html#str.split)
3. If the filename matches the given name, add it to the list of found files with `.append(xxx)`.
</details>

<details>
<summary>Super Help</summary>

```python
def find_matching_files(files, name):
    matches = []
    for f in files:
        if f.split('.')[0] == name:
            matches.append(f)
    return matches
```
</details>

### CSV Filtering
Before asking the user to enter a filename, display the list of CSV files present in the `/data` folder.
(You can use the `endswith` method to check if a filename ends with 'csv', https://docs.python.org/3/library/stdtypes.html#str.endswith)

## Exercise 2 - Reading CSV File

### File Reading
At the beginning of the program, display the list of available CSV files. Ask the user to enter a filename (without the extension). If the CSV file does not exist, display an error message and ask the user to enter a new filename.

If the file exists, read the file and display its contents. Search online for how to read a CSV file with Python.

After conducting research, you can find some explanations [here](./explications/read_files_flags_en.md)

> To go further, what should we do if we find multiple CSV files with the same name? While this is hypothetically impossible, we still need to account for this possibility. If this happens, it's an error. We can therefore raise an error: `raise ValueError("Multiple csv files found")`

<details>
<summary>Help</summary>

Official documentation: https://pythonspot.com/read-file/
A tutorial in French: https://python.doctor/page-lire-ecrire-creer-fichier-python

You will need to use the `open` function and the `readlines` method.
</details>

### Line Counting
You can remove the `print` that displays the file contents in the console.
Now, count the number of lines in the file and display the result to the user.

### Displaying Headers
Headers in a CSV file are always the first lines of the file. Display an array with the file headers.

> Remember to split the first line of the file using the `split` function.

> Be careful, the last column of the file may contain a newline character `\n`. So you need to remove this character using the `replace` function.

### Creating the Table
Perfect, now we will create a two-dimensional array with the file headers.
A two-dimensional array is an array of arrays:
```python
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
As you can see, each line of the table is itself an array.

For each line of the file, split the line with the `split` function and add the values to the table.

### Table Improvement
Now, we will improve the table. An array of arrays is not very convenient for identifying each column, as you always have to refer to the file header.

So we will create an array of dictionaries, for example:
```python
table = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

<details>
<summary>Help</summary>

To iterate through an array and get the value of each line along with its index, use the `enumerate` function.

```python
table = ["foo", "bar", "baz"]
for i, value in enumerate(table):
    print(i, value)

# 0 foo
# 1 bar
# 2 baz
```

</details>

### Using the `csv` Library
Very good, we have coded a CSV file parser, but there is a library that does this very well.
Official documentation: https://docs.python.org/3/library/csv.html

Read the documentation and replace your code that creates an array of dictionaries with the `csv` library.

> Be careful, you will need to remove all your previous code, especially `.readlines()`. Otherwise, the `csv` library might return empty arrays. This comes from the way file reading works in Python [explanations](./explications/read_file_cursor_en.md)

<details>
<summary>Help</summary>
Look towards the `csv.DictReader` function.

> If you try to display the result, you will probably see `<csv.DictReader object at 0x104d3b820>`.
> To display the result, you need to convert the result to a list using the `list` function: `print(list(table))`
</details>

## Exercise 3 - File Writing

### File Creation

We will start with a clean file (do not delete the old ones, we will need them later).

In this file, try to create a file 'test.txt' in the parsed_data folder, with the text 'Hello World'. If needed, look it up online.

### CSV File Writing

In your file, add this array of dictionaries:
```python
users = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

Now try to create a new CSV file with this array.

<details>
<summary>Help</summary>

To write a CSV file, you must first write the headers, then the rows.

To write the headers, split the keys of the first dictionary using the `keys` method and add them to the line with the `join` function.

To write the rows, retrieve the values of each user, putting them in the same order as the headers. Then add them to the line with the `join` function.

Remember to add the newline character `\n` at the end of each line.
</details>

### Using the `csv` Library
As usual, there is a library that does this very well. Use the `csv` library to write the user CSV file.

<details>
<summary>Help</summary>

Look towards the `csv.DictWriter` function. Use the `writeheader` and `writerows` methods.
</details>

## Exercise 4 - Rewriting a Column
Now that we know how to read and write files, we can manipulate them.

> From now on, the exercises will be less detailed and accompanied by a small context.

You are a developer for an online sales company. You are changing accounting software. You can transfer information from the old software to the new one using CSV files. But there is a problem with the `products.csv` file. Indeed, the value of the `archived` column is noted as `VRAI` or `FAUX`. But the new software only supports `TRUE` or `FALSE`.
So open the file with Python, modify the value of the `archived` column to `TRUE` or `FALSE` and write the new file in the `parsed_data` folder.

## Exercise 5 - Add Currency Based on Country

Again for your new accounting software, it requires a currency (EUR, USD, GBP, etc.) for each user.

Currently, in the `users.csv` file, you have the user's country. Use it to add a `currency` column, with the following values:
- FR, ES: EUR
- US: USD
- UK: GBP

## Exercise 6 - Calculate Total Purchases per User

Your sales colleague wants to run a campaign to thank your best customers. For this, they ask you for the total purchase amount for each user, and to provide the emails and names of the top 3 customers.

Create a Python script that, using the `users.csv`, `invoices.csv`, and `orders.csv` files, will display in the console the emails and names of the top 3 customers, along with their total purchase amount.

<details>
<summary>Help</summary>

To calculate the total purchases per user, read the `orders.csv` file and retrieve the price of each `invoice_id`. Then group each `invoice_id` by `user_id`, calculate the total sum, and find the top 3 (to find the top 3, you need to sort the values and take the last 3 in case of ascending order). Look towards the `sorted` function (https://docs.python.org/3/howto/sorting.html).

</details>

## Exercise 7 - Create Your Own Accounting Software (Object-Oriented Programming)

Finally, no one likes your new accounting software. So you've decided to create your own.

We will create a simplified version of an online command-line store. It will be able to read CSV files, modify them, and save them back to CSV files.

> The produced code will be a very basic and simplified approach, but it will allow practicing object-oriented programming.

We will create 4 classes, one for each CSV file:
- `User`
- `Product`
- `Order`
- `Invoice`

Each of these classes will instantiate the CSV file headers as attributes (example: a user will have attributes `id`, `lastname`, `firstname`, `email`, etc.). In the case of `Orders`, instead of storing an identifier of another object, we will directly store its instance. Example: instead of storing a `user_id`, we will directly store a `User` object.

Each class will have 3 static methods to interact with CSV files:
- `get`: which will directly retrieve the class instance based on its id and return it.
- `load`: which will read the CSV file and return a list of class instances.
- `save`: which will write the instances to the CSV file.

> For this to work, you will need to have a static `instances` attribute that will store all instances of the class.

<details>
<summary>Advice</summary>
The `load` method of `Order` will need to use the `get` methods of `Invoice` and `User`.
</details>

The program starts by triggering the `load` method of all classes.

Then, create a console menu that will allow you to:
- create a user
- create a product
- create an order (which allows entering multiple products and quantities)
- save the data

> To centralize the logic of interaction with CSV files, it is recommended to create an abstract parent class `CsvModel` that will contain the common logic of CSV file processing.

> To parse dates, it is recommended to use the `datetime` library (https://docs.python.org/3/library/datetime.html), especially the `strptime` function.

> Try to make sure the program does not crash in case of user input errors.

### To Go Further
- Add a command that allows retrieving the N biggest buyers (you may need to create more associations between classes)
- Add instance creation filters (example: email must be valid, price must be positive, etc.)
- Add additional commands (example: display all products, display all users, etc...)