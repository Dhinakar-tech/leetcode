select email from (select email, count(*) from person 
group by email
having count(*)>1) as t
