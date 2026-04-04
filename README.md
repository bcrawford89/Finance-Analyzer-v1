# Personal Finance Analyzer

A Python-based CLI tool that processes raw transaction data, cleans inconsistent financial formats, and generates meaningful summaries, insights, and visualizations.

This project demonstrates a lightweight data pipeline approach to transforming messy real-world financial data into structured, analyzable output.

---

## Features

* Cleans raw transaction data (handles `$`, commas, and inconsistent formatting)
* Converts financial data into structured numeric form
* Calculates:

  * Total income and spending
  * Spending by category
  * Net totals by month
* Generates rule-based financial insights
* Visualizes spending with a bar chart using `matplotlib`

---

## Data Pipeline Overview

```
Raw CSV → Cleaning → Analysis → Insights → Visualization
```

* **load_data.py** → reads CSV input
* **clean_data.py** → normalizes and cleans values
* **analyze.py** → computes summaries
* **insights.py** → generates observations
* **visualize.py** → produces charts
* **main.py** → orchestrates the pipeline

---

## Example Input (Before Cleaning)

| date      | description       | amount   | category  |
|-----------|-------------------|----------|-----------|
| 7/30/2025 | GALVAN'S EATERY   | -$18.55  | Food      |
| 7/30/2025 | Drive INS CO      | -$279.61 | Insurance |
| 7/31/2025 | COOPERAGE BREWING | -$18.00  | Food      |

---

## Example Output (After Processing)

```
=== Financial Summary ===

Source file: data/sample_transactions.csv

Total Income: $0.00
Total Spending: $316.16

Spending by Category:
  - Insurance: $279.61
  - Food: $36.55

Net by Month:
  - 2025-07: -316.16

Insights:
  - Highest spending category: Insurance
  - Highest spending month: 2025-07
```

A bar chart is also displayed showing spending by category.

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the program

```bash
python main.py
```

---

## Input Requirements

The CSV file must include the following columns in this order:

* `date`
* `description`
* `amount`
* `category`

### Notes

* Negative values represent spending
* Positive values represent income
* Amounts may include `$` and commas (these will automatically be cleaned)

---

## Visualization

The program generates a bar chart showing total spending by category.

---

## Project Structure

```
personal-finance-analyzer/
│── data/
│   └── sample_transactions.csv
│── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── analyze.py
│   ├── insights.py
│   ├── visualize.py
│── main.py
│── requirements.txt
│── README.md
```

---

## Key Technical Concepts Demonstrated

* Data cleaning and preprocessing using `pandas`
* Handling inconsistent real-world financial data formats
* Modular pipeline design (separation of concerns)
* Aggregation and grouping operations
* Rule-based insight generation
* Data visualization with `matplotlib`

---

## Future Improvements

* Support for multiple CSV formats (schema normalization)
* Merchant name extraction from raw transaction strings
* CLI arguments for custom file input
* Export cleaned/normalized datasets
* Anomaly detection and spending trends
* Optional AI-assisted transaction categorization

---

## Why This Project Matters

This project focuses on a real-world problem: financial data can be messy.

Instead of assuming clean inputs, it demonstrates how to:

* normalize inconsistent formats
* build reusable data processing steps
* extract meaningful insights from imperfect data

---

## License

* Apache License (Author attribution, please)

---

## Author

* Bryce Crawford

---

## NB

* All bugs and comments/suggestions can be sent to bryceecrawford@gmail.com

---

*This project takes disorganized itemized bank statement data, cleans it up, and provides insight into your spending habits*