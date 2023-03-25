import uuid
from typing import Annotated, Union, List
from fastapi import APIRouter, Header
from app.models.request.recipes import RecipeIn
from app.models.response.recipes import RecipeOut

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/")
async def get_recipes(X_HONEY_FOOD_API_KEY: Annotated[Union[str, None], Header()]) -> List[RecipeOut]:
    print(X_HONEY_FOOD_API_KEY)
    return [{"id": str(uuid.uuid4())}, {"id": str(uuid.uuid4())}]


@router.post("/")
async def add_recipe(
    recipe: RecipeIn,
    X_HONEY_FOOD_API_KEY: Annotated[Union[str, None], Header()]
) -> RecipeOut:
    print(X_HONEY_FOOD_API_KEY)
    return {"id": str(uuid.uuid4()), **recipe.dict()}


@router.get("/{id}")
async def get_recipe(
    id: str,
    X_HONEY_FOOD_API_KEY: Annotated[Union[str, None], Header()]
) -> RecipeOut:
    return {"id": id}


@router.put("/{id}")
async def update_recipe(
    id: str,
    recipe: RecipeIn,
    X_HONEY_FOOD_API_KEY: Annotated[Union[str, None], Header()]
) -> RecipeOut:
    return {"id": id}


@router.delete("/{id}")
async def delete_recipe(id: str) -> str:
    return {"id": id}