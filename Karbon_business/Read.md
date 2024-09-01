# SQL Questions

A.)Find the top 5 customers by total spend in the last 30 days.

SELECT 
   u.user_id,
    u.username,
    SUM(o.total_amount) AS total_spend

FROM 
    orders o
JOIN 
    users u ON o.user_id = u.user_id

WHERE 
    o.order_date >= CURRENT_DATE - 30

GROUP BY 
    u.user_id, u.username

ORDER BY 
    total_spend DESC

LIMIT 5;

B.)  Find Most purchased product till date.


SELECT 
    product_id,
    product_name,
    total_quantity

FROM (
    
    SELECT 
        p.product_id,
        p.product_name,
        SUM(oi.quantity) AS total_quantity,
        DENSE_RANK() OVER (ORDER BY SUM(oi.quantity) DESC) AS rank
    
    FROM 
        order_items oi
    JOIN 
        products p ON oi.product_id = p.product_id
    
    GROUP BY 
        p.product_id, p.product_name

) ranked_products

WHERE rank = 1;
