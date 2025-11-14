WITH snapshot AS (
    SELECT MAX(order_date) AS snapshot_date
    FROM orders
),
rfm AS (
    SELECT
        o.customer_id,
        (SELECT snapshot_date FROM snapshot) - MAX(o.order_date) AS recency,
        COUNT(DISTINCT o.order_id) AS frequency,
        SUM(oi.revenue) AS monetary
    FROM orders o
    JOIN order_items oi USING(order_id)
    WHERE o.order_status='Completed'
    GROUP BY o.customer_id
)
SELECT
    customer_id,
    EXTRACT(DAY FROM recency) AS recency_days,
    frequency,
    monetary
FROM rfm
ORDER BY monetary DESC;
