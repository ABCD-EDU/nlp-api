from fastapi.responses import JSONResponse
from routes.metrics import router as metrics_router
from routes.analysis import router as analysis_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, FastAPI
import uvicorn

app = FastAPI()
app_router = APIRouter()

app_router.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
app_router.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])

def add_cors(app):
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
add_cors(app)
app.include_router(app_router)
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000)

# def start_application():
#     app = FastAPI(title="ABCD-EDU API", description="ABCD-EDU", version=1.0)

#     add_cors(app)
#     # app.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
#     app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
#     return app

# app = start_application()