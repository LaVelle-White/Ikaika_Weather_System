import httpx


USGS_URL = "https://waterservices.usgs.gov/nwis/iv/"


async def fetch_gauges() -> dict:
    params = {
        "format": "json",
        "stateCd": "hi",
        "siteStatus": "active",
        "parameterCd": "00060",
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(USGS_URL, params=params)
        response.raise_for_status()
        return response.json()