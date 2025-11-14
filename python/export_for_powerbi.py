import os, shutil

PATH = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data"
DST = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\powerbi\exports"

os.makedirs(DST, exist_ok=True)

files = [
    "cleaned_customers.csv",
    "cleaned_products.csv",
    "cleaned_orders.csv",
    "cleaned_order_items.csv",
    "monthly_revenue.csv",
    "monthly_revenue.png",
    "monthly_revenue_forecast_6m.csv",
    "rfm_segments.csv"
]

for f in files:
    src = os.path.join(PATH, f)
    if os.path.exists(src):
        shutil.copy(src, DST)
        print("Exported:", f)

print("Export complete.")
