from pydantic import BaseModel, Field

class RecipeIn(BaseModel):
    title: str =  Field(title="Title", max_length=100, min_length=10)
    slug: str = Field(title="Unique Identifier", max_length=120, min_length=10)
    description: str = Field(title="Description", min_length=20, max_length=255)
    content: str = Field(title="Content", min_length=500)
    image_url: str = Field(title="Feature Image URL", min_length=10, max_length=500)
    published: bool = Field(title="Published", default=False)

