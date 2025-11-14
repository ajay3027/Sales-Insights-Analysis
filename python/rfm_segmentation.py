import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

PATH = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data"

def main():
    print("Loading cleaned CSVs...")
    orders = pd.read_csv(os.path.join(PATH,"cleaned_orders.csv"), parse_dates=["order_date"])
    order_items = pd.read_csv(os.path.join(PATH,"cleaned_order_items.csv"))

    print("Joining data...")
    tx = order_items.merge(orders, on="order_id")
    tx = tx[tx["order_status"]=="Completed"]
    tx["order_date"] = pd.to_datetime(tx["order_date"])
    tx["revenue"] = tx["revenue"].astype(float)

    print("Computing RFM...")
    snapshot = tx["order_date"].max() + pd.Timedelta(days=1)
    rfm = tx.groupby("customer_id").agg({
        "order_date": lambda x: (snapshot - x.max()).days,
        "order_id": "nunique",
        "revenue": "sum"
    }).reset_index()
    rfm.columns = ["customer_id","recency","frequency","monetary"]

    print("Clustering...")
    X = rfm[["recency","frequency","monetary"]].fillna(0)
    X_log = np.log1p(X)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_log)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto").fit(X_scaled)
    rfm["segment_k"] = kmeans.labels_

    rfm.to_csv(os.path.join(PATH,"rfm_segments.csv"), index=False)
    print("Saved rfm_segments.csv")

if __name__ == "__main__":
    main()
