import csv
import json

def read_sales_data(csv_path):
    sales_data = []
    try:
        with open(csv_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append(row)
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return sales_data


def read_product_data(json_path):
    product_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            product_data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_path}")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as e:
        print(f"Error reading JSON: {e}")
    return product_data
