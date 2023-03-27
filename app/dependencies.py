import json
from typing import Annotated
from fastapi import Header
from fastapi import Request
from app.models.base import settings
from app.errors import HTTPExceptionResponse


async def valid_api_key_required(request: Request, X_HONEY_FOOD_API_KEY: Annotated[str, Header()]):
    if X_HONEY_FOOD_API_KEY != settings.X_HONEY_FOOD_API_KEY:
        raise HTTPExceptionResponse(status=403,code="INVALID_API_KEY", message="Invalid X_HONEY_FOOD_API_KEY Header")

    request.state.user = json.loads(settings.X_API_USER_INFO)