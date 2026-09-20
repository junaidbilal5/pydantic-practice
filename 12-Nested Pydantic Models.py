from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str
    postal_code: str


class Employee(BaseModel):
    name: str
    age: int
    address: Address


employee = Employee(
    name="Junaid",
    age=30,
    address={
        "city": "Berlin",
        "country": "Germany",
        "postal_code": "10115"
    }
)

print(employee)



print(employee.address.city)
print(employee.address.country)