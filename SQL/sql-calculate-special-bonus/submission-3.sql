-- Write your query below

select employee_id,
CASE 
    WHEN employee_id % 2 = 1 AND name not like 'M%' then salary
    else 0
END AS bonus
from employees
ORDER BY employee_id;