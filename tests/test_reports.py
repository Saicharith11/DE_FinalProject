import pandas as pd

from src.reports import create_reports


def test_create_reports_calculates_product_sales():
    test_data = pd.DataFrame(
        {
            "order_date": pd.to_datetime(["2025-01-01", "2025-01-02"]),
            "customer": ["Aarav", "Diya"],
            "product": ["Mouse", "Mouse"],
            "category": ["Electronics", "Electronics"],
            "city": ["Delhi", "Mumbai"],
            "sales_amount": [500, 300],
        }
    )

    top_products, _, _, _, _ = create_reports(test_data)

    assert top_products["sales_amount"].iloc[0] == 800
