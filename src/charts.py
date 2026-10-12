import matplotlib.pyplot as plt

from config import OUTPUT_FOLDER


def create_charts(city_sales, category_sales, monthly_sales):
    """Create, save, and display simple sales charts."""
    plt.figure(figsize=(8, 5))
    plt.bar(city_sales["city"], city_sales["sales_amount"], color="#002A5B")
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/sales_by_city.png")
    print(f"Chart saved: {OUTPUT_FOLDER}/sales_by_city.png")

    plt.figure(figsize=(8, 5))
    plt.bar(category_sales["category"], category_sales["sales_amount"], color="#FF5C43")
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales Amount")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/sales_by_category.png")
    print(f"Chart saved: {OUTPUT_FOLDER}/sales_by_category.png")

    plt.figure(figsize=(8, 5))
    plt.plot(monthly_sales["month"], monthly_sales["sales_amount"], marker="o", color="#FF5C43")
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount")
    plt.grid(color="#D9E2EC")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FOLDER}/monthly_sales_chart.png")
    print(f"Chart saved: {OUTPUT_FOLDER}/monthly_sales_chart.png")

    plt.show()
