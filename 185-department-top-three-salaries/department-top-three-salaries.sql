 with salary_rank as (select e.id, e.name as Employee, e.salary, d.name as Department, dense_rank()over(partition by d.id order by e.salary desc  ) as ranks 
from employee as e
inner join department as d
on e.departmentId = d.id )
select department, employee, salary from salary_rank 
where ranks<=3;