select 
distinct 
customer_id, customer_name 
from customers AS c 

Where c.customer_id IN(
 
    SELECT customer_id FROM orders WHERE product_name = 'A'
    INTERSECT
    SELECT customer_id FROM orders WHERE product_name = 'B'


    EXCEPT 
    SELECT customer_id FROM orders WHERE product_name = 'C'
)

Order by c.customer_name