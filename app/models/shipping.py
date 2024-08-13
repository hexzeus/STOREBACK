from pydantic import BaseModel


class ShippingItem(BaseModel):
    external_variant_id: str
    quantity: int


class ShippingRequest(BaseModel):
    recipient: dict
    items: list[ShippingItem]


class TaxRequest(BaseModel):
    shipping: str
    recipient: dict
    items: list[ShippingItem]
