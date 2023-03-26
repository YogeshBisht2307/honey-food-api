from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from errors import HTTPExceptionResponse

from routers import recipes


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

@app.exception_handler(HTTPExceptionResponse)
async def unicorn_exception_handler(exc: HTTPExceptionResponse):
    return JSONResponse(
        status_code=exc.status,
        content={"code": exc.code,"message": exc.message}
)
