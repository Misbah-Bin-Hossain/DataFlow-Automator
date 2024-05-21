import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    csv_file = 'profiles1.csv'
    json_file = 'data.json'
    min_rows = 900

    csv_to_json(csv_file, json_file)
    print("\nNew json file name-profiles1.json is created \n")

