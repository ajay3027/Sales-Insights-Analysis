import pandas as pd
import matplotlib.pyplot as plt
import os

PATH = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data"

def main():
    print("Loading cleaned CSVs...")
    customers = pd.read_csv(os.path.join(PATH,"cleaned_customers.csv"), parse_dates=["join_date"])
    products = pd.read_csv(os.path.join(PATH,"cleaned_products.csv"))
    orders = pd.read_csv(os.path.join(PATH,"cleaned_orders.csv"), parse_dates=["order_date"])
    order_items = pd.read_csv(os.path.join(PATH,"cleaned_order_items.csv"))

    print("Joining tables...")
    tx = order_items.merge(orders, on="order_id").merge(products, on="product_id")
    tx = tx[tx["order_status"]=="Completed"]
    tx["order_date"] = pd.to_datetime(tx["order_date"])
    tx["revenue"] = tx["revenue"].astype(float)

    print("Calculating monthly revenue...")
    monthly = tx.set_index("order_date").resample("M")["revenue"].sum().reset_index()
    monthly.columns = ["month","total_revenue"]

    monthly.to_csv(os.path.join(PATH,"monthly_revenue.csv"), index=False)
    print("Saved monthly_revenue.csv")

    plt.figure(figsize=(10,4))
    plt.plot(monthly["month"], monthly["total_revenue"])
    plt.tight_layout()
    plt.savefig(os.path.join(PATH,"monthly_revenue.png"))
    print("Saved monthly_revenue.png")

if __name__ == "__main__":
    main()
