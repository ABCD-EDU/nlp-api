from fastapi.responses import JSONResponse
from routes.metrics import router as metrics_router
from routes.analysis import router as analysis_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
import uvicorn


def add_cors(app_):
    origins = ["*"]
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app = FastAPI()
if __name__ == "__main__":
    app_router = APIRouter()
    app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
    app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"]) 
    add_cors(app) 
    uvicorn.run(app, host="127.0.0.1", port=8000)
