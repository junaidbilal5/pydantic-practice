from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float


employee = Employee(
    name="Junaid",
    age="30",
    salary="65000"
)

print(employee)
print(type(employee.age))
print(type(employee.salary))