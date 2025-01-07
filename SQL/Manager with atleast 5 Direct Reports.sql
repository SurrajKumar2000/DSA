# Write your MySQL query statement below
select a.name as name
from Employee a
cross join Employee b
where a.id=b.managerId
group by b.managerId
having count(b.managerId)>=5

