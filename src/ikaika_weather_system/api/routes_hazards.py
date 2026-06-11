from fastapi import APIRouter

from ikaika_weather_system.models.hazard import Hazard
from ikaika_weather_system.services.hazard_service import get_active_hazards

router = APIRouter(prefix="/hazards", tags=["hazards"])


@router.get("", response_model=list[Hazard])
async def read_hazards():
    return await get_active_hazards()