# Sales Data Analysis

A Python and Pandas project that cleans a sales dataset and creates simple sales reports. This project was built for the **Sales Data Analysis - Python + Pandas** assessment.

## Setup

- Python 3.11.4
- Libraries listed in `requirements.txt`

Install the project libraries:

```powershell
py -m pip install -r requirements.txt
```


## How to run the project

Open a terminal in the `sales_analysis` folder and run:

```powershell
py main.py
```

The program displays data checks and reports in the terminal. It also saves CSV reports, audit reports, and charts in `output/`.

## Project files

- `sales.csv` - input dataset
- `main.py` - runs the complete project
- `config.py` - stores common input, output, and log paths
- `src/` - contains the data loading, validation, transformation, reporting, chart, logging, and outlier modules
- `tests/` - contains Pytest test files
- `output/` - contains generated CSV files and PNG charts
- `logs/` - contains the application log file
- `docs/` - contains presentation and summary PDF documents

## Data cleaning decisions

The original dataset contains 123 rows. After cleaning, 114 rows are used for analysis.

- Exact duplicate rows are removed.
- Missing customer and city values are changed to `Unknown` so the sale can still be included.
- Rows with a missing or invalid date are removed.
- Rows with a missing, zero, or negative price are removed.
- Rows with a zero or negative quantity are removed.
- Dates are converted to a proper date type before monthly sales are calculated.

## Calculations and reports

For every valid row, the project calculates:

```text
sales_amount = quantity * price
```

It then calculates total sales, average order value, top 5 products by sales, top 5 customers by sales, sales by city, sales by category, and monthly sales.

## Output files

The following files are created in `output/` every time the program runs:

- `sales_summary.csv` - total sales and average order value
- `customer_summary.csv` - top 5 customers by sales
- `product_summary.csv` - top 5 products by sales
- `city_summary.csv` - sales by city
- `monthly_sales.csv` - sales by month
- `data_quality_summary.csv` - data-quality checks and actions taken
- `outlier_report.csv` - IQR-based quantity and price outlier review

Sales by category is displayed in the terminal. The assessment requires the calculation, but does not require a separate category CSV file.

## Run tests

```powershell
py -m pytest
```
