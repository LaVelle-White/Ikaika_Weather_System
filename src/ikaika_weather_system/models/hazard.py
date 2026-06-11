from pydantic import BaseModel


class Hazard(BaseModel):
    id: str
    title: str
    severity: str | None = None
    source: str
    area_desc: str | None = None