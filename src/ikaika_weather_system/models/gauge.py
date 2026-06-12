from pydantic import BaseModel


class Gauge(BaseModel):
    site_code: str
    site_name: str
    latest_value: float | None = None
    unit: str | None = None
    observed_at: str | None = None
    latitude: float | None = None
    longitude: float | None = None