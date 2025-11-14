WITH first_order AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM orders
    WHERE order_status = 'Completed'
    GROUP BY customer_id
),
revenues AS (
    SELECT
        fo.customer_id,
        fo.first_order_date,
        o.order_date,
        SUM(oi.revenue) AS revenue
    FROM first_order fo
    JOIN orders o ON o.customer_id = fo.customer_id
    JOIN order_items oi USING(order_id)
    WHERE o.order_status='Completed'
      AND o.order_date <= fo.first_order_date + INTERVAL '365 days'
    GROUP BY 1,2,3
)
SELECT
    first_order_date,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(SUM(revenue)::numeric,2) AS total_revenue,
    ROUND(SUM(revenue)/NULLIF(COUNT(DISTINCT customer_id),0),2) AS avg_ltv_365
FROM revenues
GROUP BY 1
ORDER BY first_order_date;
