from employees import Employee
from db import conn


first_user = Employee.get(1)
if first_user is None:
    first_user = Employee("name", "surname", "age")
    first_user.save()

first_user.name = "Tornike"
first_user.save()
emp1 = Employee("nikoloz", "kurdadze", 19, pk=1)
emp1.save()
conn.commit()
conn.close()
