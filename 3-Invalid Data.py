from pydantic import BaseModel, ValidationError


class Employee(BaseModel):
    name: str
    age: int
    salary: float


try:
    employee = Employee(
        name="Junaid",
        age="abc",
        salary="hello"
    )

except ValidationError as e:
    print(e)