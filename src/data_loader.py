import pandas as pd


def load_sales_data(file_name, logger):
    """Read and display a basic overview of the sales data."""
    required_columns = [
        "order_id",
        "order_date",
        "customer",
        "product",
        "category",
        "quantity",
        "price",
        "city",
    ]

    try:
        data = pd.read_csv(file_name)
    except FileNotFoundError:
        logger.error("Input file not found: %s", file_name)
        print(f"Error: The input file '{file_name}' was not found.")
        return None
    except Exception as error:
        logger.error("Could not read %s: %s", file_name, error)
        print(f"Error: Could not read '{file_name}'.")
        return None

    missing_columns = [
        column for column in required_columns if column not in data.columns
    ]
    if missing_columns:
        logger.error("Required columns missing: %s", ", ".join(missing_columns))
        print("Error: Required columns are missing:", ", ".join(missing_columns))
        return None

    logger.info("Sales data loaded successfully: %s rows", len(data))

    print("\n--- First 5 rows ---")
    print(data.head())
    print("\n--- Dataset information ---")
    data.info()
    print("\n--- Missing values per column ---")
    print(data.isnull().sum())
    print("\n--- Duplicate rows ---")
    print(data.duplicated().sum())

    return data
