import pandas as pd


def clean_sales_data(data):
    """Clean the sales data before calculations are performed."""
    cleaned_data = data.drop_duplicates().copy() # exact duplicates are removed

    # rows become from 123 to 120 after removing duplicates 

    cleaned_data["customer"] = cleaned_data["customer"].fillna("Unknown") #if name is missing it is replaced with "Unknown"

    cleaned_data["city"] = cleaned_data["city"].fillna("Unknown") #if city is missing it is replaced with "Unknown"

    cleaned_data["order_date"] = pd.to_datetime(
        cleaned_data["order_date"], errors="coerce", format="mixed"
    ) # convert order_date to datetime, invalid parsing will be set as NaT(coerce)
    # mixed for format because the data has multiple formats for order_date

    cleaned_data = cleaned_data.dropna(subset=["order_date", "price"])
    # removed rows with missing order_date or price 
    # ( 2 missing or invalid dates and 1 missing price)
    # 120 becomes 117 after removing rows with missing order_date or price

    cleaned_data = cleaned_data[
        (cleaned_data["quantity"] > 0) & (cleaned_data["price"] > 0)
    ] # removes rows with negative quantity or price 
    #( 1 negative quantity , 1 negative prices and 1 zero quantity)
    # 117 becomes 114 after removing rows with non-positive quantity or price

    return cleaned_data


def add_sales_amount(data):
    """Add sales_amount by multiplying quantity and price."""
    data = data.copy()
    data["sales_amount"] = data["quantity"] * data["price"]
    return data
