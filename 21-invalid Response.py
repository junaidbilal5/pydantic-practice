from _20_Complete_LLM_Validation_Example import Movie

from pydantic import ValidationError


llm_response2 = {
    "title": "Inception",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 15
}




try:

    movie = Movie.model_validate(llm_response2)

    print("Valid response l2")
    print(movie)

except ValidationError as e:

    print("Invalid response l2")
    print(e)