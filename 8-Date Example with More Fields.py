from datetime import date
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    joining_date: date
    birth_date: date
    salary: float


employee = Employee(
    name="Junaid",
    joining_date="2025-10-15",
    birth_date="1990-05-20",
    salary=65000
)

print(employee)