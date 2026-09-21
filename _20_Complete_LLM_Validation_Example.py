from pydantic import BaseModel, Field, ValidationError


class Movie(BaseModel):
    title: str = Field(min_length=1)
    year: int = Field(gt=1888)
    genre: str
    rating: float = Field(ge=0, le=10)


llm_response = {
    "title": "Inception",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8
}


try:

    movie = Movie.model_validate(llm_response)

    print("Valid response")
    print(movie)

except ValidationError as e:

    print("Invalid response")
    print(e)