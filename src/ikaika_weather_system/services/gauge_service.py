from ikaika_weather_system.connectors.usgs import fetch_gauges
from ikaika_weather_system.models.gauge import Gauge


async def get_gauges() -> list[Gauge]:
    raw_data = await fetch_gauges()
    time_series = raw_data.get("value", {}).get("timeSeries", [])

    gauges = []

    for series in time_series:
        source_info = series.get("sourceInfo", {})
        site_code = source_info.get("siteCode", [{}])[0].get("value", "")
        site_name = source_info.get("siteName", "")
        geo = source_info.get("geoLocation", {}).get("geogLocation", {})
        latitude = float(geo.get("latitude")) if geo.get("latitude") else None
        longitude = float(geo.get("longitude")) if geo.get("longitude") else None

        values_block = series.get("values", [])
        latest_value = None
        observed_at = None

        if values_block and values_block[0].get("value"):
            latest_observation = values_block[0]["value"][-1]
            latest_value = float(latest_observation["value"]) if latest_observation.get("value") else None
            observed_at = latest_observation.get("dateTime")

        variable = series.get("variable", {})
        unit = variable.get("unit", {}).get("unitCode")

        gauges.append(
            Gauge(
                site_code=site_code,
                site_name=site_name,
                latest_value=latest_value,
                unit=unit,
                observed_at=observed_at,
                latitude=latitude,
                longitude=longitude,
            )
        )

    return gauges