from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float
    department: str


employee = Employee(
    name="Junaid",
    age=30,
    salary=65000,
    department="Data Engineering"
)

print(employee)


print(employee.name)
print(employee.age)
print(employee.salary)