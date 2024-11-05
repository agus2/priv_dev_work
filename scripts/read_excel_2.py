import pandas as pd

def extract_tables(file_path):
    tables = []
    df = pd.read_excel(file_path, skiprows=0)  # Read the first table
    tables.append(df)
    for i in range(1, 10):  # Try reading up to 100 tables
        try:
            df = pd.read_excel(file_path, skiprows=i)
            tables.append(df)
        except pd.errors.EmptyDataError:
            break  # No more tables, stop reading
    return tables

# Usage example
file_path = "ejem.xlsx" #file_path = "path/to/your/excel_file.xlsx"
tables = extract_tables(file_path)
for i, table in enumerate(tables):
    print(f"Table {i+1}:")
    print(table.head())  # Print the first few rows of each table