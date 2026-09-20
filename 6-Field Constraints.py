from pydantic import BaseModel, Field


class Employee(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=18, lt=65)
    salary: float = Field(gt=0)
    department: str



employee = Employee(
    name="J",
    age=30,
    salary=65000,
    department="Data Engineering"
)

print(employee)