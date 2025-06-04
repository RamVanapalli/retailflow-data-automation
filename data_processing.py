from datetime import datetime

def clean_sales_data(raw_sales):
    cleaned = []

    for row in raw_sales:
        # Skip if product_id is missing
        if not row.get("product_id"):
            continue

        # Fix date format
        date_str = row.get("date", "")
        try:
            if "/" in date_str:
                date_obj = datetime.strptime(date_str, "%m/%d/%Y")
            else:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            row["date"] = date_obj.strftime("%Y-%m-%d")
        except:
            # skip row if date is totally broken
            continue

        # Convert quantity and sale_amount
        try:
            row["quantity"] = int(row["quantity"])
        except:
            row["quantity"] = 0

        try:
            row["sale_amount"] = round(float(row["sale_amount"]), 2)
        except:
            row["sale_amount"] = 0.0

        cleaned.append(row)

    return cleaned
