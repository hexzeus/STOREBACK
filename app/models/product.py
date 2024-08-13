from pydantic import BaseModel


class ProductModel(BaseModel):
    id: str
    name: str
    description: str
    price: float
    image_url: str


class ProductVariant(BaseModel):
    id: str
    name: str
    price: float


class ProductDetail(BaseModel):
    product: ProductModel
    variants: list[ProductVariant]
