SELECT (
    SELECT MAX(salary)
    FROM (
        SELECT salary,
               DENSE_RANK() OVER (ORDER BY salary DESC) AS ranks
        FROM employee
    ) t
    WHERE ranks = 2
) AS SecondHighestSalary;
