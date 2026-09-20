from pydantic import BaseModel, model_validator


class Employee(BaseModel):
    name: str
    salary: float
    bonus: float

    @model_validator(mode="after")
    def validate_compensation(self):

        if self.bonus > self.salary:
            raise ValueError(
                "Bonus cannot be greater than salary"
            )

        return self


employee = Employee(
    name="Junaid",
    salary=65000,
    bonus=10000
)

print(employee)






#employee = Employee(
#    name="Junaid",
#    salary=65000,
#    bonus=70000
#)