import pandas as pd


def find_outliers(data):
    """Find unusual quantity or price values using the IQR method."""
    outlier_rows = []

    for column in ["quantity", "price"]:
        first_quartile = data[column].quantile(0.25)
        third_quartile = data[column].quantile(0.75)
        interquartile_range = third_quartile - first_quartile
        lower_limit = first_quartile - 1.5 * interquartile_range
        upper_limit = third_quartile + 1.5 * interquartile_range

        outliers = data[(data[column] < lower_limit) | (data[column] > upper_limit)].copy()
        outliers["outlier_column"] = column
        outliers["lower_limit"] = lower_limit
        outliers["upper_limit"] = upper_limit
        outlier_rows.append(outliers)

    return pd.concat(outlier_rows, ignore_index=True)
