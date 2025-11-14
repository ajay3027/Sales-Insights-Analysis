SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.revenue) AS revenue,
    SUM(oi.qty) AS total_qty
FROM order_items oi
JOIN orders o USING(order_id)
JOIN products p USING(product_id)
WHERE o.order_status = 'Completed'
GROUP BY
    p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;
