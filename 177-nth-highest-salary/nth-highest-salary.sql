CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select  DISTINCT salary  from 
      (select salary, dense_rank()over(order by salary desc) as rnk from Employee) as t
      where rnk = N
  );
END