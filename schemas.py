from pydantic import BaseModel

class RecordCreate(BaseModel):
    name: str
    description: str