import pandas as pd

from src.transformations import add_sales_amount, clean_sales_data


def test_clean_sales_data():
    test_data = pd.DataFrame(
        {
            "order_id": ["O1", "O1", "O2", "O3", "O4"],
            "order_date": [
                "2025-01-01",
                "2025-01-01",
                "2025-01-02",
                "2025-01-03",
                "2025-01-04",
            ],
            "customer": ["Aarav", "Aarav", "Diya", "Rohan", None],
            "product": ["Mouse", "Mouse", "Cable", "Lamp", "Bottle"],
            "category": ["Electronics", "Electronics", "Electronics", "Home", "Home"],
            "quantity": [1, 1, 0, 2, 1],
            "price": [500, 500, 200, -100, 300],
            "city": ["Delhi", "Delhi", "Mumbai", "Pune", None],
        }
    )

    cleaned_data = clean_sales_data(test_data)

    assert len(cleaned_data) == 2
    assert "Unknown" in cleaned_data["customer"].values
    assert "Unknown" in cleaned_data["city"].values


def test_add_sales_amount():
    test_data = pd.DataFrame({"quantity": [2], "price": [150]})

    result = add_sales_amount(test_data)

    assert result["sales_amount"].iloc[0] == 300


def test_clean_sales_data_removes_invalid_dates():
    test_data = pd.DataFrame(
        {
            "order_id": ["O1", "O2", "O3"],
            "order_date": ["2025-01-01", "not_a_date", None],
            "customer": ["Aarav", "Diya", "Rohan"],
            "product": ["Mouse", "Cable", "Lamp"],
            "category": ["Electronics", "Electronics", "Home"],
            "quantity": [1, 1, 1],
            "price": [500, 200, 1000],
            "city": ["Delhi", "Mumbai", "Pune"],
        }
    )

    cleaned_data = clean_sales_data(test_data)

    assert len(cleaned_data) == 1
    assert cleaned_data["order_id"].iloc[0] == "O1"
