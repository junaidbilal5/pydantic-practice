from datetime import date
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    joining_date: date


employee = Employee(
    name="Junaid",
    joining_date="2025-10-15"
)

print(employee)
print(employee.joining_date)
print(type(employee.joining_date))