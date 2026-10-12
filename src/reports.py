import pandas as pd

from config import OUTPUT_FOLDER


def create_reports(data):
    """Create the grouped sales reports required by the project."""
    product_sales = data.groupby("product", as_index=False)["sales_amount"].sum()
    top_products = product_sales.sort_values("sales_amount", ascending=False).head(5)

    customer_sales = data.groupby("customer", as_index=False)["sales_amount"].sum()
    top_customers = customer_sales.sort_values("sales_amount", ascending=False).head(5)

    city_sales = data.groupby("city", as_index=False)["sales_amount"].sum()
    city_sales = city_sales.sort_values("sales_amount", ascending=False)

    category_sales = data.groupby("category", as_index=False)["sales_amount"].sum()
    category_sales = category_sales.sort_values("sales_amount", ascending=False)

    data = data.copy()
    data["month"] = data["order_date"].dt.strftime("%Y-%m")
    monthly_sales = data.groupby("month", as_index=False)["sales_amount"].sum()

    return top_products, top_customers, city_sales, category_sales, monthly_sales


def export_reports(total_sales, average_order_value, top_products, top_customers,
                   city_sales, monthly_sales):
    """Save the required report tables as CSV files."""
    sales_summary = pd.DataFrame(
        {"total_sales": [round(total_sales, 2)],
         "average_order_value": [round(average_order_value, 2)]}
    )
    sales_summary.to_csv(f"{OUTPUT_FOLDER}/sales_summary.csv", index=False)
    top_customers.to_csv(f"{OUTPUT_FOLDER}/customer_summary.csv", index=False)
    top_products.to_csv(f"{OUTPUT_FOLDER}/product_summary.csv", index=False)
    city_sales.to_csv(f"{OUTPUT_FOLDER}/city_summary.csv", index=False)
    monthly_sales.to_csv(f"{OUTPUT_FOLDER}/monthly_sales.csv", index=False)
