import csv
import json

def test_csv_columns(csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        return len(header) == 12

def test_csv_rows(csv_file, min_rows):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        num_rows = sum(1 for row in reader)
        return num_rows > min_rows

def test_json_properties(json_file):
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)
        return all(len(row) == 12 for row in data)

def test_json_rows(json_file, min_rows):
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)
        return len(data) > min_rows

if __name__ == "__main__":
    csv_file = 'profiles1.csv'
    json_file = 'data.json'
    min_rows = 900

    
    print("CSV columns test (There is 12 columbs) -", test_csv_columns(csv_file))
    print("CSV rows test (there is more then 900 rows) -", test_csv_rows(csv_file, min_rows))
    print("JSON properties test (There is 12 columbs) -", test_json_properties(json_file))
    print("JSON rows test (there is more then 900 rows) -", test_json_rows(json_file, min_rows))