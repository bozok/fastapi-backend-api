# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # If needed

from app.core.config import settings
# from app.api.routes.api import api_router # Will add later

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=settings.DEBUG,
)

# --- CORS ---
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    
# --- Routers ---
# app.include_router(api_router, prefix=settings.API_V1_STR) # Will add later


# Basic root endpoint / health check
@app.get("/", tags=["Health Check"])
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}!"}

# --- Optional: Add other app setup logic here ---
# For example, startup/shutdown events, mounting static files, etc.