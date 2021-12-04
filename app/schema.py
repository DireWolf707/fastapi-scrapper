from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductSchema(BaseModel):
    asin:str
    title:Optional[str]

class ProductScrapeEventSchema(ProductSchema):
    uuid:UUID

class ProductListSchema(ProductSchema):
    pass

class ProductDetailSchema(ProductSchema):
    price_str:Optional[str]