from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    department: str
    email: str | None = None




employee = Employee(
    name="Junaid",
    age=30,
    department="Data Engineering"
)

print(employee)