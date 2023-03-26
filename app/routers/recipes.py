import uuid
from typing import Annotated, Union, List
from fastapi import APIRouter, Header, Depends, Request
from app.models.request.recipes import RecipeIn
from app.models.response.recipes import RecipeOut
from app.dependencies import valid_api_key_required


router = APIRouter(dependencies=[Depends(valid_api_key_required)])


@router.get("/")
async def get_recipes(request: Request) -> List[RecipeOut]:
    return [
        RecipeOut(**{
            "id": str(uuid.uuid4()),
            "title": "stringstri",
            "slug": "stringstri",
            "description": "stringstringstringst",
            "content": "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringst",
            "image_type": "application/octet-stream",
            "published": True,
            "created": 0,
            "updated": 0
       }),
       RecipeOut(**{
            "id": str(uuid.uuid4()),
            "title": "stringstri",
            "slug": "stringstri",
            "description": "stringstringstringst",
            "content": "stringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringstringst",
            "image_type": "application/octet-stream",
            "published": True,
            "created": 0,
            "updated": 0
        })
    ]


@router.post("/")
async def add_recipe(request: Request, recipe: RecipeIn) -> RecipeOut:
    print(request)
    return {"id": str(uuid.uuid4())}


@router.get("/{id}")
async def get_recipe(id: str, request: Request) -> RecipeOut:
    return {"id": id}


@router.put("/{id}")
async def update_recipe(id: str, request: Request, recipe: RecipeIn) -> RecipeOut:
    return {"id": id}


@router.delete("/{id}")
async def delete_recipe(id: str, request: Request,) -> str:
    return {"id": id}
