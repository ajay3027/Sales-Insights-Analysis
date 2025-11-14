WITH orders_m AS (
  SELECT customer_id,
         DATE_TRUNC('month', order_date)::date AS month
  FROM orders
  WHERE order_status='Completed'
  GROUP BY 1,2
),
cohorts AS (
  SELECT
      customer_id,
      MIN(month) OVER (PARTITION BY customer_id) AS cohort_month,
      month
  FROM orders_m
)
SELECT
    cohort_month,
    month,
    COUNT(DISTINCT customer_id) AS customers
FROM cohorts
GROUP BY 1,2
ORDER BY 1,2;
