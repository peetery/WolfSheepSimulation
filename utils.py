import json
import csv

def save_to_json(data, filename='pos.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename='alive.csv'):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["round_no", "alive_sheep"])
        writer.writerows(data)
    print(f"Data saved to {filename}")