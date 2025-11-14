WITH daily AS (
  SELECT
      DATE_TRUNC('day', o.order_date)::date AS day,
      SUM(oi.revenue) AS revenue
  FROM orders o
  JOIN order_items oi USING(order_id)
  WHERE o.order_status='Completed'
  GROUP BY 1
)
SELECT
    day,
    revenue,
    AVG(revenue) OVER (
        ORDER BY day
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d,
    CASE
        WHEN revenue >
             2 * AVG(revenue) OVER (ORDER BY day ROWS BETWEEN 29 PRECEDING AND CURRENT ROW)
        THEN TRUE
        ELSE FALSE
    END AS anomaly_flag
FROM daily
ORDER BY day;
