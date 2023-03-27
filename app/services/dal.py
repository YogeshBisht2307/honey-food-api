import uuid
from typing import List, Union
from datetime import datetime
from app.services.clients import db_client, datastore
from app.models.database.recipes import RecipeDB
from google.cloud.datastore.query import PropertyFilter


def without_id(data_dict: dict) -> dict:
    del data_dict["id"]
    return data_dict


def get_recipe_by_slug(slug: str) -> Union[RecipeDB, None]:
    query = db_client.query(kind="Recipe").add_filter(filter=PropertyFilter("slug", "=", slug))
    recipes = [RecipeDB(**{"id": recipe.key.name, **dict(recipe)}) for recipe in list(query.fetch())]
    if not recipes:
        return None

    return recipes[0]


def create_recipe(recipe: dict) -> RecipeDB:
    recipe: RecipeDB = RecipeDB(**{"id": str(uuid.uuid4()), **dict(recipe)})
    entity = datastore.Entity(
        db_client.key('Recipe', recipe.id),
        exclude_from_indexes=("description", "content", "title", "updated", "image_url")
    )
    entity.update(without_id(recipe.dict()))
    db_client.put(entity)
    return recipe


def get_recipes(user_id: str) -> List[RecipeDB]:
    query = db_client.query(kind="Recipe").add_filter(filter=PropertyFilter("user_id", "=", user_id))
    return [RecipeDB(**{"id": recipe.key.name, **dict(recipe)}) for recipe in list(query.fetch())]


def update_recipe_by_slug(slug: str, recipe: dict) -> Union[RecipeDB, None]:
    recipe_entity = get_recipe_by_slug(slug)
    if not recipe_entity:
        return None

    recipe_entity = recipe_entity.copy(update=recipe)
    entity = datastore.Entity(db_client.key("Recipe", recipe_entity.id))
    entity.update({"updated": (datetime.utcnow().timestamp() * 1000), **without_id(recipe_entity.dict())})
    db_client.put(entity)
    return RecipeDB(**{"id": entity.key.name, **dict(entity)})

def delete_recipe_by_slug(slug: str) -> Union[bool, None]:
    recipe_entity = get_recipe_by_slug(slug)
    if not recipe_entity:
        return None

    entity = datastore.Entity(db_client.key("Recipe", recipe_entity.id))
    db_client.delete(entity.key)
    return True


