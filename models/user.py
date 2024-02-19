from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
  id: Optional[int] = None
  username: str = Field(max_length=100)
  email: str = Field(max_length=100)
  password: str = Field(max_length=100)
  is_active: bool = True

