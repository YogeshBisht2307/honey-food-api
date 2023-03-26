from typing import List

from fastapi import APIRouter, Depends, Request
from models.request.recipes import RecipeIn
from models.response.recipes import RecipeOut
from models.response.recipes import ResponseOut
from models.database.recipes import RecipeDB

from services import dal
from errors import HTTPExceptionResponse
from dependencies import valid_api_key_required


router = APIRouter(
    dependencies=[Depends(valid_api_key_required)],
    responses={400: {"model": ResponseOut}}
)


@router.get("/")
async def get_recipes(request: Request) -> List[RecipeOut]:
    recipe_entities =  dal.get_recipes(request.state.user['id'])

    recipes: List = []
    for recipe_entity in recipe_entities:
        recipes.append(RecipeOut(**{
            "title": recipe_entity.title,
            "slug": recipe_entity.slug,
            "description": recipe_entity.description,
            "content": recipe_entity.content,
            "image_type": recipe_entity.image_type,
            "published": recipe_entity.published,
            "user_id": recipe_entity.user_id,
            "created": recipe_entity.created,
            "updated": recipe_entity.updated
        }))

    return recipes


@router.post("/")
async def add_recipe(request: Request, recipe: RecipeIn) -> RecipeOut:
    recipe_entity: RecipeDB = dal.get_recipe_by_slug(recipe.slug)
    if recipe_entity:
        raise HTTPExceptionResponse(
            status=400,
            code="UNQIUE_SLUG_CONSTRAINT_FAILURE",
            message="Recipe already exists with sam slug"
        )

    recipe_entity = dal.create_recipe({**recipe.dict(), "user_id": request.state.user['id']})
    if not recipe_entity:
        raise HTTPExceptionResponse(
            status=500,
            code="ADD_RECIPE_FAILURE",
            message="Unable to add recipe."
        )

    return RecipeOut(**{
        "title": recipe_entity.title,
        "slug": recipe_entity.slug,
        "description": recipe_entity.description,
        "content": recipe_entity.content,
        "image_type": recipe_entity.image_type,
        "published": recipe_entity.published,
        "user_id": recipe_entity.user_id,
        "created": recipe_entity.created,
        "updated": recipe_entity.updated
    })


@router.get("/{slug}")
async def get_recipe(slug: str, request: Request) -> RecipeOut:
    recipe_entity: RecipeDB = dal.get_recipe_by_slug(slug)
    if not recipe_entity:
        raise HTTPExceptionResponse(
            status=400,
            code="DOES_NOT_EXISTS",
            message="Recipe doesn't exists."
        )

    return RecipeOut(**{
        "title": recipe_entity.title,
        "slug": recipe_entity.slug,
        "description": recipe_entity.description,
        "content": recipe_entity.content,
        "image_type": recipe_entity.image_type,
        "published": recipe_entity.published,
        "user_id": recipe_entity.user_id,
        "created": recipe_entity.created,
        "updated": recipe_entity.updated
    })


@router.put("/{slug}")
async def update_recipe(slug: str, request: Request, recipe: RecipeIn) -> RecipeOut:
    recipe_entity: RecipeDB = dal.update_recipe_by_slug(slug, recipe.dict())
    if not recipe_entity:
        raise HTTPExceptionResponse(
            status=400,
            code="DOES_NOT_EXISTS",
            message="Recipe doesn't exists."
        )

    return RecipeOut(**{
        "title": recipe_entity.title,
        "slug": recipe_entity.slug,
        "description": recipe_entity.description,
        "content": recipe_entity.content,
        "image_type": recipe_entity.image_type,
        "published": recipe_entity.published,
        "user_id": recipe_entity.user_id,
        "created": recipe_entity.created,
        "updated": recipe_entity.updated
    })


@router.delete("/{slug}")
async def delete_recipe(slug: str, request: Request,) -> ResponseOut:
    return ResponseOut(code="DELETED", message="Recipe deleted successfully")
