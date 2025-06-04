import unittest
from data_processing import clean_sales_data
from data_enrichment import enrich_sales_data
from process_data import aggregate_sales

class TestDataProcessing(unittest.TestCase):

    def test_clean_sales_data(self):
        raw = [
            {"date": "03/04/2023", "transaction_id": "TX01", "product_id": "P001", "quantity": "2", "sale_amount": "40.00"},
            {"date": "2023-03-02", "transaction_id": "TX02", "product_id": "", "quantity": "1", "sale_amount": "20.00"},
            {"date": "wrong", "transaction_id": "TX03", "product_id": "P001", "quantity": "1", "sale_amount": "10.00"},
        ]
        cleaned = clean_sales_data(raw)
        self.assertEqual(len(cleaned), 1)
        self.assertEqual(cleaned[0]["date"], "2023-03-04")
        self.assertEqual(cleaned[0]["quantity"], 2)
        self.assertEqual(cleaned[0]["sale_amount"], 40.00)

    def test_enrich_sales_data(self):
        sales = [{"product_id": "P002", "quantity": 1, "sale_amount": 25.0}]
        products = [{"product_id": "P002", "category": "Gadgets"}]
        enriched = enrich_sales_data(sales, products)
        self.assertEqual(enriched[0]["category"], "Gadgets")

    def test_aggregate_sales(self):
        enriched = [
            {"category": "Gadgets", "sale_amount": 25.0, "quantity": 2},
            {"category": "Gadgets", "sale_amount": 75.0, "quantity": 3},
            {"category": "Tools", "sale_amount": 40.0, "quantity": 1}
        ]
        result = aggregate_sales(enriched)
        for row in result:
            if row["category"] == "Gadgets":
                self.assertEqual(row["total_transactions"], 2)
                self.assertEqual(row["total_quantity"], 5)
                self.assertEqual(row["total_sales"], "100.00")
                self.assertEqual(row["average_transaction_value"], "50.00")
            elif row["category"] == "Tools":
                self.assertEqual(row["total_sales"], "40.00")


if __name__ == '__main__':
    unittest.main()
