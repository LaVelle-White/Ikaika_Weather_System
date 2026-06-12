from fastapi import APIRouter

from ikaika_weather_system.models.gauge import Gauge
from ikaika_weather_system.services.gauge_service import get_gauges


router = APIRouter()


@router.get("/gauges", response_model=list[Gauge])
async def read_gauges():
    return await get_gauges()