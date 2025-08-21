select e.unique_id, em.name from EmployeeUNI as e
right join Employees as em 
on em.id = e.id

