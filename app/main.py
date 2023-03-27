from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.errors import HTTPExceptionResponse, http_exception_handler

from app.routers import recipes


# v1 API
apiv1 = FastAPI(docs_url=None, redoc_url="/docs")
apiv1.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
apiv1.add_exception_handler(HTTPExceptionResponse, http_exception_handler)


app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/api/v1", apiv1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
