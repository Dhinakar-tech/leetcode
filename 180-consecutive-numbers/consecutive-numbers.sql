with firstvalue as 
(select id, num, LEAD(num)over(order by id) as 'NEXT1' from logS),
second_value as
(select *, lEAD(NEXT1)over(order by id) as 'NEXT2' from firstvalue) 
-- select * from second_value;
select  DISTINCT num as ConsecutiveNums from second_value 
where num = NEXT1 and NEXT1 = NEXT2;