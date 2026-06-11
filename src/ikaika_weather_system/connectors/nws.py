import httpx


NWS_ALERTS_URL = "https://api.weather.gov/alerts/active"


async def fetch_active_alerts() -> dict:
    headers = {
        "User-Agent": "ikaika-weather-system/0.1 (lavelle.white@student.chaminade.edu)",
        "Accept": "application/geo+json",
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(NWS_ALERTS_URL, headers=headers)
        response.raise_for_status()
        return response.json()