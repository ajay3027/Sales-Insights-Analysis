import pandas as pd
import os

RAW = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data_raw"
OUT = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data"

def load_csv(name, dates=None):
    path = os.path.join(RAW, name)
    print("Loading:", path)
    df = pd.read_csv(path, parse_dates=dates)
    print("Loaded:", name, "| Rows:", len(df))
    return df

def main():
    customers = load_csv("customers.csv", ["join_date"])
    products = load_csv("products.csv")
    orders = load_csv("orders.csv", ["order_date"])
    order_items = load_csv("order_items.csv")

    orders = orders.dropna(subset=["order_id","customer_id","order_date"])

    customers.to_csv(os.path.join(OUT, "cleaned_customers.csv"), index=False)
    print("Saved cleaned_customers.csv")

    products.to_csv(os.path.join(OUT, "cleaned_products.csv"), index=False)
    print("Saved cleaned_products.csv")

    orders.to_csv(os.path.join(OUT, "cleaned_orders.csv"), index=False)
    print("Saved cleaned_orders.csv")

    order_items.to_csv(os.path.join(OUT, "cleaned_order_items.csv"), index=False)
    print("Saved cleaned_order_items.csv")

if __name__ == "__main__":
    main()
