from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str
    postal_code: str


class Department(BaseModel):
    name: str
    manager: str


class Employee(BaseModel):
    name: str
    age: int
    address: Address
    department: Department



employee = Employee(
    name="Junaid",
    age=30,

    address={
        "city": "Berlin",
        "country": "Germany",
        "postal_code": "10115"
    },

    department={
        "name": "Data Engineering",
        "manager": "John"
    }
)

print(employee)