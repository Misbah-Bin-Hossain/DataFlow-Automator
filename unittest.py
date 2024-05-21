import csv
import json
import sys

def test_csv_columns(csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        if len(header) != 12:
            print("Error: CSV does not have exactly 12 columns.")
            sys.exit(1)
        return True

def test_csv_rows(csv_file, min_rows):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        num_rows = sum(1 for row in reader)
        if num_rows <= min_rows:
            print(f"Error: CSV does not have more than {min_rows} rows.")
            sys.exit(1)
        return True

def test_json_properties(json_file):
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)
        if not all(len(row) == 12 for row in data):
            print("Error: Not all JSON objects have exactly 12 properties.")
            sys.exit(1)
        return True

def test_json_rows(json_file, min_rows):
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)
        if len(data) <= min_rows:
            print(f"Error: JSON does not have more than {min_rows} rows.")
            sys.exit(1)
        return True

if __name__ == "__main__":
    csv_file = 'profiles1.csv'
    json_file = 'data.json'
    min_rows =900

    if test_csv_columns(csv_file):
        print("CSV columns test passed (12 columns).")
    
    if test_csv_rows(csv_file, min_rows):
        print("CSV rows test passed (more than 900 rows).")
    
    if test_json_properties(json_file):
        print("JSON properties test passed (12 properties per object).")
    
    if test_json_rows(json_file, min_rows):
        print("JSON rows test passed (more than 900 rows).")
