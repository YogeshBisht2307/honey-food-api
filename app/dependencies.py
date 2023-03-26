from typing import Annotated
from fastapi import HTTPException, Header
from fastapi import Request


async def valid_api_key_required(request: Request, X_HONEY_FOOD_API_KEY: Annotated[str, Header()]):
    if X_HONEY_FOOD_API_KEY != "fake-super-secret-key":
        raise HTTPException(status_code=403, detail="Invalid X_HONEY_FOOD_API_KEY Header")

    request.state.user = {"name": "Yogesh", "email": "yogeshbisht.2307@gmail.com"}