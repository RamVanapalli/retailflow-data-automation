# RetailFlow: Data Automation for Sales Reporting
I've named this assignment "RetailFlow" as I want to keep this project as a mini-ETL pipeline and facilitate my storytelling with data.

This project simulates a small retail data processing workflow, where I worked on:
1. Data ingestion,
2. cleaning,
3. enriching, and
4. Summarising the sales data.

**I. Project Overview:**
A retail company receives daily sales transactions (in CSV) and product details (in JSON format). My task was to build a system that:

- Reads and cleans the sales data
- Normalises and enriches it using product metadata
- Aggregates key metrics per category
- Outputs a final report as a CSV

The goal wasn’t just to “make it work” but to do it in a modular, testable, and beginner-friendly way — while sticking mostly to Python’s built-in features (as required).


Breaking down the task:(Flow)
I've divided my solution into four phases:
Phase 1: Core Logic Development (Modules) 
Phase 2: Orchestration & Scripting (main process_data.py scrip)
Phase 3: Testing phase
Phase 4: Documentation (aggregated_report)

**II. Files and What They Do**

- `process_data.py` – Main script that runs the entire workflow
- `data_ingestion.py` – Loads CSV and JSON data
- `data_processing.py` – Cleans date formats, missing fields, and types
- `data_enrichment.py` – Merges product info into sales rows
- `test_data_processing.py` – Basic unit tests to validate logic
- `sales_data.csv` – Sample input (daily transactions)
- `product_data.json` – Sample input (product master list)
- `aggregated_report.csv` – Final report (generated after running the script)
- `README.md` – This file

**III. How to Run?**

You’ll need Python 3.11+ installed. No external libraries required.

1. Clone or download the repo
2. Open a terminal in the project folder
3. Run the script:
```
python process_data.py
```
Now, it’ll ask you for the input file paths (they are in the same folder):
Input:
sales_data.csv
product_data.json

The output will be saved as aggregated_report.csv.

**Output Format:**
The final CSV contains one row per product category with:

-category

-total_sales

-total_transactions

-average_transaction_value

-total_quantity

**IV. Running Tests:**
To check the logic, run:
```
python test_data_processing.py
```
The tests check:

1. If date formats and types are cleaned correctly

2. Whether product info merges properly

3. If the aggregation logic is calculating expected results

**Final Thoughts**
This assignment gave me a good chance to think through how small automations work in real business settings, especially when dealing with messy real-world data. It would be more fun working with huge datasets- bigger problems, smarter solutions and better insights.

If you’re reviewing this, thank you, B-Stock, for the opportunity.
