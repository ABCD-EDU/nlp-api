from routes import analysis
from routes import metrics
from fastapi import APIRouter

app_router = APIRouter()

app_router.include_router(analysis.router, prefix="/analysis",tags=['metrics'])
app_router.include_router(metrics.router, prefix="/metrics",tags=['metrics'])