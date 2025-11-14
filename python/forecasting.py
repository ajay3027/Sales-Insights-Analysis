import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import os

PATH = r"C:\Users\dell\OneDrive\Desktop\Repo\Sales-Insights-Analysis\data"

def main():
    print("Loading monthly revenue...")
    monthly = pd.read_csv(os.path.join(PATH,"monthly_revenue.csv"), parse_dates=["month"])
    monthly = monthly.set_index("month").asfreq("MS").fillna(0)

    ts = monthly["total_revenue"]

    print("Fitting SARIMAX model...")
    model = SARIMAX(ts, order=(1,1,1), seasonal_order=(1,1,1,12),
                    enforce_stationarity=False, enforce_invertibility=False)
    res = model.fit(disp=False)

    pred = res.get_forecast(steps=6)
    pred_mean = pred.predicted_mean
    pred_ci = pred.conf_int()

    forecast = pd.DataFrame({
        "month": pred_mean.index,
        "forecast_revenue": pred_mean.values,
        "ci_lower": pred_ci.iloc[:,0].values,
        "ci_upper": pred_ci.iloc[:,1].values
    })

    forecast.to_csv(os.path.join(PATH,"monthly_revenue_forecast_6m.csv"), index=False)
    print("Saved monthly_revenue_forecast_6m.csv")

if __name__ == "__main__":
    main()
