from ikaika_weather_system.connectors.nws import fetch_active_alerts
from ikaika_weather_system.models.hazard import Hazard


async def get_active_hazards() -> list[Hazard]:
    payload = await fetch_active_alerts()
    features = payload.get("features", [])

    hazards: list[Hazard] = []

    for feature in features[:20]:
        properties = feature.get("properties", {})
        hazards.append(
          Hazard(
    id=str(feature.get("id") or ""),
    title=properties.get("headline") or properties.get("event") or "Untitled hazard",
    severity=properties.get("severity") or "Unknown",
    source=properties.get("senderName") or "NWS",
    area_desc=properties.get("areaDesc") or "",
)
        )

    return hazards