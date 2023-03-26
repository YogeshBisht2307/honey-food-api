from typing import Annotated
from fastapi import Header
from fastapi import Request
from errors import HTTPExceptionResponse


async def valid_api_key_required(request: Request, X_HONEY_FOOD_API_KEY: Annotated[str, Header()]):
    if X_HONEY_FOOD_API_KEY != "NAkJDX7YhjV4zLJG6y87mHKdM6NhJgwoujwwb5fI":
        raise HTTPExceptionResponse(status=403,code="INVALID_API_KEY", message="Invalid X_HONEY_FOOD_API_KEY Header")

    request.state.user = {
        "id": "cc748ee1-5317-4e36-9812-92210a62f2ea",
        "name": "Yogesh",
        "email": "yogeshbisht.2307@gmail.com"
    }