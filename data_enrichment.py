def enrich_sales_data(clean_sales, product_list):
    enriched = []

    # Make a quick lookup dict: product_id → product_info
    product_lookup = {p["product_id"]: p for p in product_list}

    for row in clean_sales:
        pid = row.get("product_id")
        product = product_lookup.get(pid)

        if not product:
            continue  # skip if product details not found

        # Add category to sales row
        row["category"] = product.get("category", "Unknown")
        enriched.append(row)

    return enriched
