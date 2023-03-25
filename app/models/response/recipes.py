from pydantic import BaseModel, Field

class RecipeOut(BaseModel):
    title: str =  Field(title="Title", max_length=100, min_length=10)
    slug: str = Field(title="Unique Identifier", max_length=120, min_length=10)
    description: str = Field(title="Description", min_length=20, max_length=255)
    content: str = Field(title="Content", min_length=500)
    image_type: str = Field(title="Feature Image Content Type", default="application/octet-stream", min_length=3, max_length=25)
    published: bool = Field(title="Published")
    created: int = Field(title="Millis From Epoch")
    updated: int = Field(title="Millis From Epoch")

