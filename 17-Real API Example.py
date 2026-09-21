from pydantic import BaseModel



class Employee(BaseModel):
    name: str
    age: int
    salary: float
    department: str




api_response = {
    "name": "Junaid",
    "age": 30,
    "salary": 65000,
    "department": "Data Engineering"
}


employee = Employee.model_validate(api_response)