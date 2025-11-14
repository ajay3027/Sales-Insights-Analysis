SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.revenue) AS total_revenue
FROM orders o
JOIN order_items oi USING(order_id)
WHERE o.order_status = 'Completed'
GROUP BY 1
ORDER BY 1;
