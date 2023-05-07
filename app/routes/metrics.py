from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import fetch_metrics

router = APIRouter()

@router.get("/")
async def get_metrics():
    # metrics = fetch_metrics()
    return {"hotdog":"hello"}
    # return JSONResponse(content=metrics)
