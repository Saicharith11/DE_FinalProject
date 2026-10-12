from config import INPUT_FILE, OUTPUT_FOLDER
from src.charts import create_charts
from src.data_loader import load_sales_data
from src.data_validator import check_data_quality, create_data_quality_summary
from src.logger_setup import setup_logger
from src.outlier_detection import find_outliers
from src.reports import create_reports, export_reports
from src.transformations import add_sales_amount, clean_sales_data


logger = setup_logger()
logger.info("Sales Data Analysis project started")

# Load and check the raw sales data.
sales_data = load_sales_data(INPUT_FILE, logger)

if sales_data is None:
    logger.error("Project stopped because the input data could not be loaded")
    raise SystemExit

check_data_quality(sales_data)

# Save the audit report before cleaning the data.
data_quality_summary = create_data_quality_summary(sales_data)
data_quality_summary.to_csv(
    f"{OUTPUT_FOLDER}/data_quality_summary.csv", index=False
)
print(f"Data-quality audit saved: {OUTPUT_FOLDER}/data_quality_summary.csv")
logger.info("Data-quality audit report exported")

cleaned_sales_data = clean_sales_data(sales_data)
print("\nClean rows ready for analysis:", len(cleaned_sales_data))
logger.info("Data cleaning completed: %s clean rows", len(cleaned_sales_data))

# Add the sales value for each clean record.
cleaned_sales_data = add_sales_amount(cleaned_sales_data)

outlier_report = find_outliers(cleaned_sales_data)
outlier_report.to_csv(f"{OUTPUT_FOLDER}/outlier_report.csv", index=False)
print(f"Outlier report saved: {OUTPUT_FOLDER}/outlier_report.csv")
logger.info("Outlier report exported: %s rows", len(outlier_report))

total_sales = cleaned_sales_data["sales_amount"].sum()
average_order_value = cleaned_sales_data["sales_amount"].mean()

print("Total sales:", round(total_sales, 2))
print("Average order value:", round(average_order_value, 2))

top_products, top_customers, city_sales, category_sales, monthly_sales = create_reports(
    cleaned_sales_data
)

# Display the main analysis results.
print("\n--- Top 5 products by sales ---")
print(top_products)
print("\n--- Top 5 customers by sales ---")
print(top_customers)
print("\n--- Sales by city ---")
print(city_sales)
print("\n--- Sales by category ---")
print(category_sales)
print("\n--- Monthly sales ---")
print(monthly_sales)

export_reports(
    total_sales,
    average_order_value,
    top_products,
    top_customers,
    city_sales,
    monthly_sales,
)
print("\nCSV report files saved in the output folder.")
logger.info("Sales report CSV files exported")

create_charts(city_sales, category_sales, monthly_sales)
logger.info("Charts created and saved successfully")
