from pydantic import BaseModel
from typing import List, Optional


class Person(BaseModel):
    id: str
    name: str
    email: str
    age: Optional[int] = None
    interests: Optional[List[str]] = []