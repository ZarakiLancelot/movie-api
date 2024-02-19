from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
  id: Optional[int] = None
  title: str = Field(max_length=100)
  release_year: int = Field(ge=1950, le=2100)
  category: str = Field(max_length=20)
  rating: float

  class Config:
    json_schema_extra = {
      "example": {
        "id": 1,
        "title": "The Matrix",
        "release_year": 1994,
        "category": "Action",
        "rating": 9.3
      }
    }
