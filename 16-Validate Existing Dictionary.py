from pydantic import BaseModel


data = {
    "name": "Junaid",
    "age": 30,
    "salary": 65000
}



class Employee(BaseModel):
    name: str
    age: int
    salary: float


employee = Employee.model_validate(data)

print(employee)