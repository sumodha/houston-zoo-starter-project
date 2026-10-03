from pydantic import BaseModel, ConfigDict


class ExhibitResponse(BaseModel):
    id: int
    name: str
    location: str
    description: str

    model_config = ConfigDict(from_attributes=True)