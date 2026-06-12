from fastapi import APIRouter

from ikaika_weather_system.services.summary_service import build_daily_brief


router = APIRouter()


@router.post("/summaries/daily-brief")
async def create_daily_brief():
    return await build_daily_brief()