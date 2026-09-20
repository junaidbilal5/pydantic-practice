from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    department: str = "Data Engineering"


employee = Employee(
    name="Junaid",
    age=30
)

print(employee.department)