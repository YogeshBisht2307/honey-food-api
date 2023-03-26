from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import recipes


# v1 API
apiv1 = FastAPI()
apiv1.include_router(recipes.router, prefix="/recipes", tags=["recipes"])



app = FastAPI()
app.mount("/api/v1", apiv1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
