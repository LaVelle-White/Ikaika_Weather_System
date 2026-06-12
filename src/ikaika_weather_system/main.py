from fastapi import FastAPI
from ikaika_weather_system.api.routes_health import router as health_router
from ikaika_weather_system.api.routes_hazards import router as hazards_router
from ikaika_weather_system.api.routes_gauges import router as gauges_router

app = FastAPI(title="Ikaika Weather System")

app.include_router(health_router)
app.include_router(hazards_router)
app.include_router(gauges_router)