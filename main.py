from fastapi.responses import JSONResponse
from routes.metrics import router as metrics_router
from routes.analysis import router as analysis_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
import uvicorn

from routes.base import app_router

def include_router(app):
    app.include_router(app_router)

def add_cors(app_):
    origins = ["*"]
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def start_application():
    app = FastAPI(title="ABCD-EDU API", description="ABCD-EDU", version=1.0)
    include_router(app)
    add_cors(app)
    
    return app

app = start_application()

