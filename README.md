# Pydantic Practice — Data Validation for Data & AI Engineering

A practical hands-on guide to **Pydantic v2** for data validation, structured data, API payloads, nested models, and LLM structured outputs.

This project is designed for Data Engineers and AI/Data Engineers who want to understand how Pydantic can be used to create reliable data contracts and validate incoming data.

---

## 📌 What is Pydantic?

[Pydantic](https://docs.pydantic.dev/) is a Python library used for **data validation and data parsing** based on Python type hints.

Instead of manually checking every input:

```python
if not isinstance(age, int):
    ...
```

we can define a model:

```python
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float
```

Pydantic then validates incoming data against this model.

---

# 🎯 What This Project Covers

* Basic Pydantic models
* Type validation
* Optional fields
* Default values
* Field constraints
* Date validation
* Custom field validation
* Model-level validation
* Nested Pydantic models
* Dictionary validation
* JSON serialization
* Error handling
* Structured LLM outputs
* Pydantic as a data contract

---

# 🛠️ Project Setup

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd pydantic-practice
```

## 2. Create a virtual environment

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install pydantic
```

Or, if using a requirements file:

```bash
pip install -r requirements.txt
```

---

# 📁 Project Structure

```text
pydantic-practice/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 1️⃣ Basic Pydantic Model

A Pydantic model is created by inheriting from `BaseModel`.

```python
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    salary: float
    department: str
```

Create an object:

```python
employee = Employee(
    name="Junaid",
    age=30,
    salary=65000,
    department="Data Engineering"
)

print(employee)
```

Pydantic validates the data according to the model definition.

---

# 2️⃣ Type Validation

Pydantic uses Python type hints to define expected types.

```python
class Employee(BaseModel):
    name: str
    age: int
    salary: float
```

Input:

```python
employee = Employee(
    name="Junaid",
    age="30",
    salary="65000"
)
```

Pydantic can convert compatible values.

For example:

```text
"30"     → 30
"65000"  → 65000.0
```

You can check the resulting types:

```python
print(type(employee.age))
print(type(employee.salary))
```

---

# 3️⃣ Handling Validation Errors

Invalid data produces a `ValidationError`.

```python
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
```

This is useful when validating:

* API requests
* JSON data
* Database records
* Configuration
* External service responses
* LLM outputs

---

# 4️⃣ Optional Fields

A field can be optional.

```python
class Employee(BaseModel):
    name: str
    age: int
    department: str
    email: str | None = None
```

Now this is valid:

```python
employee = Employee(
    name="Junaid",
    age=30,
    department="Data Engineering"
)
```

The email will have the value:

```python
None
```

---

# 5️⃣ Default Values

Fields can have default values.

```python
class Employee(BaseModel):
    name: str
    age: int
    department: str = "Data Engineering"
```

Now:

```python
employee = Employee(
    name="Junaid",
    age=30
)
```

will automatically use:

```text
Data Engineering
```

for the department.

---

# 6️⃣ Field Constraints

`Field()` allows us to define additional validation rules.

```python
from pydantic import BaseModel, Field


class Employee(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=18, lt=65)
    salary: float = Field(gt=0)
    department: str
```

### Common constraints

```text
min_length=2
```

String must contain at least two characters.

```text
gt=18
```

Value must be greater than 18.

```text
lt=65
```

Value must be less than 65.

```text
gt=0
```

Salary must be greater than zero.

---

# 7️⃣ Date Validation

Pydantic can validate and parse dates.

```python
from datetime import date
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    joining_date: date
```

Input:

```python
employee = Employee(
    name="Junaid",
    joining_date="2025-10-15"
)
```

Pydantic converts the string into a Python `date` object.

```python
print(employee.joining_date)
print(type(employee.joining_date))
```

---

# 8️⃣ Custom Field Validation

Use `field_validator` when built-in validation isn't enough.

Example:

> An employee must be at least 18 years old.

```python
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
```

The important part is:

```python
@field_validator("age")
```

It tells Pydantic:

> Run this validation function whenever the `age` field is processed.

---

# 9️⃣ Custom Email Validation

Multiple validators can be defined.

```python
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

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):

        if "@" not in value:
            raise ValueError(
                "Invalid email address"
            )

        return value
```

---

# 🔟 Model-Level Validation

Sometimes validation requires multiple fields.

For example:

> Bonus cannot be greater than salary.

Use `model_validator`.

```python
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
```

The difference is:

```text
field_validator
        ↓
Validates individual fields


model_validator
        ↓
Validates relationships between fields
```

---

# 1️⃣1️⃣ Nested Models

Pydantic supports complex nested structures.

```python
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str
    postal_code: str


class Employee(BaseModel):
    name: str
    age: int
    address: Address
```

Input:

```python
employee = Employee(
    name="Junaid",
    age=30,
    address={
        "city": "Berlin",
        "country": "Germany",
        "postal_code": "10115"
    }
)
```

Access nested data:

```python
print(employee.address.city)
print(employee.address.country)
```

---

# 1️⃣2️⃣ Multiple Nested Models

Real-world API responses often contain multiple levels of nested data.

```python
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
```

Input:

```python
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
```

This allows Pydantic to validate the complete nested structure.

---

# 1️⃣3️⃣ Convert Model to Dictionary

Use:

```python
employee.model_dump()
```

Example:

```python
data = employee.model_dump()

print(data)
```

Result:

```python
{
    "name": "Junaid",
    "age": 30,
    "address": {
        "city": "Berlin",
        "country": "Germany",
        "postal_code": "10115"
    }
}
```

---

# 1️⃣4️⃣ Convert Model to JSON

Use:

```python
json_data = employee.model_dump_json()

print(json_data)
```

This is useful when sending structured data to APIs or other systems.

---

# 1️⃣5️⃣ Validate an Existing Dictionary

A very common Data Engineering scenario is receiving data from an API.

```python
data = {
    "name": "Junaid",
    "age": 30,
    "salary": 65000
}
```

Define the schema:

```python
class Employee(BaseModel):
    name: str
    age: int
    salary: float
```

Validate:

```python
employee = Employee.model_validate(data)

print(employee)
```

The workflow is:

```text
API
 ↓
JSON
 ↓
Python Dictionary
 ↓
Pydantic
 ↓
Validated Object
 ↓
Data Pipeline
```

---

# 1️⃣6️⃣ Pydantic + LLM Structured Output

Pydantic is especially useful in AI Engineering.

Suppose an LLM is asked to extract movie information.

We expect:

```text
title
year
genre
rating
```

Define the schema:

```python
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: float = Field(ge=0, le=10)
```

Example LLM response:

```python
llm_response = {
    "title": "Inception",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8
}
```

Validate it:

```python
movie = Movie.model_validate(llm_response)

print(movie)
```

Now the application has a structured and validated object.

---

# 1️⃣7️⃣ Why Validate LLM Output?

LLMs can return unexpected data.

For example:

```python
llm_response = {
    "title": "Inception",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 15
}
```

But our model says:

```python
rating: float = Field(ge=0, le=10)
```

Therefore:

```text
0 <= rating <= 10
```

The invalid response will be rejected.

This creates a useful boundary:

```text
LLM
 ↓
Structured Response
 ↓
Pydantic Validation
 ↓
Valid Data
 ↓
Application / Database / Pipeline
```

---

# 🧠 Key Concepts to Remember

| Concept             | Purpose                           |
| ------------------- | --------------------------------- |
| `BaseModel`         | Define a data model               |
| Type hints          | Define expected types             |
| `Field()`           | Add constraints                   |
| `ValidationError`   | Handle invalid data               |
| `field_validator`   | Validate specific fields          |
| `model_validator`   | Validate multiple fields together |
| Nested models       | Validate complex structures       |
| `model_validate()`  | Validate existing data            |
| `model_dump()`      | Model → dictionary                |
| `model_dump_json()` | Model → JSON                      |
| `date`              | Validate date fields              |
| Optional fields     | Allow missing/`None` values       |
| Structured output   | Validate LLM responses            |

---

# 🔥 Data Engineering Use Cases

Pydantic can be used at the boundary of a data or AI application.

### API Data

```text
REST API
   ↓
JSON
   ↓
Pydantic
   ↓
Validation
   ↓
Data Processing
```

### Event Data

```text
Kafka Event
    ↓
Pydantic
    ↓
Schema Validation
    ↓
Spark / Python Processing
```

### LLM Applications

```text
User Prompt
    ↓
LLM
    ↓
Structured JSON
    ↓
Pydantic
    ↓
Validation
    ↓
Database / API
```

### Configuration

```text
config.json
    ↓
Pydantic
    ↓
Validation
    ↓
Application
```

---

# 🎯 Interview Explanation

A concise interview answer:

> Pydantic is a Python library for data validation and parsing based on type hints. I can define a Pydantic model as a data contract and validate incoming API payloads, configuration, event data, or LLM responses against that contract. I can use `Field` for constraints, `field_validator` for custom field-level rules, and `model_validator` when validation depends on multiple fields. After validation, I can use `model_dump()` or `model_dump_json()` to serialize the validated object.

For AI Engineering:

> Pydantic is particularly useful for structured LLM outputs because instead of trusting arbitrary text from an LLM, I can define the expected schema and validate the response before passing it to downstream application logic.

---

# 🚀 Recommended Learning Order

Practice these in this order:

```text
1. BaseModel
      ↓
2. Type validation
      ↓
3. Optional / default fields
      ↓
4. Field constraints
      ↓
5. Dates
      ↓
6. field_validator
      ↓
7. model_validator
      ↓
8. Nested models
      ↓
9. model_validate()
      ↓
10. model_dump()
      ↓
11. JSON serialization
      ↓
12. LLM structured output
```

The most important concepts for your **Data Engineering + AI Engineering preparation** are:

**`BaseModel` → `Field` → `field_validator` → `model_validator` → nested models → `model_validate()` → structured LLM output.**
