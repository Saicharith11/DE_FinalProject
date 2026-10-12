import pandas as pd


def get_converted_dates(data):
    """Convert dates so invalid values become missing date values."""
    return pd.to_datetime(data["order_date"], errors="coerce", format="mixed")


def check_data_quality(data):
    """Show the data-quality problems that need to be cleaned."""
    print("\n--- Missing values ---")
    print(data.isnull().sum())
    print("\n--- Duplicate rows ---")
    print(data.duplicated().sum())
    print("\n--- Invalid quantities (zero or negative) ---")
    print(data.loc[data["quantity"] <= 0, ["order_id", "quantity"]])
    print("\n--- Invalid prices (zero or negative) ---")
    print(data.loc[data["price"] <= 0, ["order_id", "price"]])

    converted_dates = get_converted_dates(data)
    invalid_dates = data["order_date"].notna() & converted_dates.isna()
    print("\n--- Invalid dates ---")
    print(data.loc[invalid_dates, ["order_id", "order_date"]])


def create_data_quality_summary(data):
    """Create a simple summary of data-quality checks and actions."""
    converted_dates = get_converted_dates(data)

    return pd.DataFrame(
        {
            "check": [
                "Duplicate rows", "Missing customer", "Missing city",
                "Missing or invalid date", "Missing price", "Invalid quantity",
                "Invalid price",
            ],
            "count": [
                data.duplicated().sum(), data["customer"].isnull().sum(),
                data["city"].isnull().sum(), converted_dates.isnull().sum(),
                data["price"].isnull().sum(), (data["quantity"] <= 0).sum(),
                (data["price"] <= 0).sum(),
            ],
            "action_taken": [
                "Removed", "Replaced with Unknown", "Replaced with Unknown",
                "Removed", "Removed", "Removed", "Removed",
            ],
        }
    )
