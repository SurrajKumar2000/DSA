SELECT  b.unique_id,a.name
FROM Employees a
left join EmployeeUNI b
on a.id=b.id
