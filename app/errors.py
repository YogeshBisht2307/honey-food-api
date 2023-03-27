from fastapi import Request
from fastapi.responses import JSONResponse


class HTTPExceptionResponse(Exception):
    def __init__(self, status: int, code: str, message: str):
        self.status = status
        self.code = code
        self.message = message


async def http_exception_handler(request: Request, exc: HTTPExceptionResponse):
    return JSONResponse(
        status_code=exc.status,
        content={"code": exc.code,"message": exc.message}
)