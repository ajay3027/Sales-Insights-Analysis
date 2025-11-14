CREATE MATERIALIZED VIEW mv_monthly_revenue AS
SELECT
    DATE_TRUNC('month', o.order_date)::date AS month,
    SUM(oi.revenue) AS revenue
FROM orders o
JOIN order_items oi USING(order_id)
WHERE o.order_status='Completed'
GROUP BY 1;

-- Refresh when needed:
-- REFRESH MATERIALIZED VIEW mv_monthly_revenue;
