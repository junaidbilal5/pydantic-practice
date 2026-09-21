from _13_Multiple_Nested_Objects import (
    Address,
    Department,
    Employee
)


employee = Employee(
    name="Junaid",
    age=30,
    address=Address(
        city="Berlin",
        country="Germany",
        postal_code="10115"
    ),
    department=Department(
        name="Data Engineering",
        manager="John"
    )
)


data = employee.model_dump()

print(data)
print(type(data))