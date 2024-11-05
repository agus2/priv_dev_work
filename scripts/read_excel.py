import pandas as pd

def iterate_excel_rows(file_path):
    try:
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            print(f"Row {index}:")
            print("Properties:")
            for col_name, value in row.items():
                print(f"{col_name}: {value}")
            # Perform any necessary operations on the row data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"No data found in file: {file_path}")

# Usage example
file_path = "ejem.xlsx" #"path/to/your/excel_file.xlsx"
iterate_excel_rows(file_path)