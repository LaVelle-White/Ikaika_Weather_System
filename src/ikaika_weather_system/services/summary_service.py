from datetime import datetime, timezone

from ikaika_weather_system.services.hazard_service import get_active_hazards
from ikaika_weather_system.services.gauge_service import get_gauges


async def build_daily_brief() -> dict:
    hazards = await get_active_hazards()
    gauges = await get_gauges()

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "hazard_count": len(hazards),
        "gauge_count": len(gauges),
        "summary": f"Today there are {len(hazards)} active hazard records and {len(gauges)} gauge records in the system.",
    }