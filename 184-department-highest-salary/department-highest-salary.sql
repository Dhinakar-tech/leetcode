with salary_rank as (select e.id, e.name  as Employee, salary, d.name as Department, rank()over(partition by d.id order by e.salary desc  ) as ranks from employee as e
inner join department as d
on e.departmentid = d.id)
select department, employee, salary from salary_rank
where ranks = 1;
