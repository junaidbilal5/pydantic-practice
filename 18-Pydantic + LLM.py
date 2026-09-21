from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str
    year: int
    genre: str
    rating: float = Field(ge=0, le=10)


llm_response = {
    "title": "Inception",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8
}



movie = Movie.model_validate(llm_response)

print(movie)