from fastapi import FastAPI
from ikaika_weather_system.api.routes_health import router as health_router

app = FastAPI(title="Ikaika Weather System")

app.include_router(health_router)