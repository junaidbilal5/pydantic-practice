from pydantic import BaseModel, field_validator


class Employee(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):

        if value < 18:
            raise ValueError(
                "Employee must be at least 18 years old"
            )

        return value