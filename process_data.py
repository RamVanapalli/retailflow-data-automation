import sys
from collections import defaultdict
import csv

from data_ingestion import read_sales_data, read_product_data
from data_processing import clean_sales_data
from data_enrichment import enrich_sales_data

def aggregate_sales(sales):
    summary = defaultdict(lambda: {
        "total_sales": 0.0,
        "total_transactions": 0,
        "total_quantity": 0
    })

    for row in sales:
        cat = row["category"]
        summary[cat]["total_sales"] += row["sale_amount"]
        summary[cat]["total_transactions"] += 1
        summary[cat]["total_quantity"] += row["quantity"]

    # Build final list
    result = []
    for category, data in summary.items():
        avg = data["total_sales"] / data["total_transactions"] if data["total_transactions"] else 0
        result.append({
            "category": category,
            "total_sales": f"{data['total_sales']:.2f}",
            "total_transactions": data["total_transactions"],
            "average_transaction_value": f"{avg:.2f}",
            "total_quantity": data["total_quantity"]
        })

    # Sort alphabetically
    result.sort(key=lambda x: x["category"])
    return result


def write_report(aggregated_data, output_file="aggregated_report.csv"):
    fields = [
        "category",
        "total_sales",
        "total_transactions",
        "average_transaction_value",
        "total_quantity"
    ]
    try:
        with open(output_file, mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            for row in aggregated_data:
                writer.writerow(row)
    except Exception as e:
        print(f"Error writing CSV: {e}")


def main():
    # Ask for file paths
    sales_path = input("Enter path to sales CSV: ").strip()
    product_path = input("Enter path to product JSON: ").strip()

    raw_sales = read_sales_data(sales_path)
    products = read_product_data(product_path)

    cleaned_sales = clean_sales_data(raw_sales)
    enriched_sales = enrich_sales_data(cleaned_sales, products)

    final_summary = aggregate_sales(enriched_sales)
    write_report(final_summary)

    print("Report written to 'aggregated_report.csv'")


if __name__ == "__main__":
    main()
