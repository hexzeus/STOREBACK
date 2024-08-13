from pydantic import BaseModel


class OrderItem(BaseModel):
    id: str
    quantity: int


class ShippingAddress(BaseModel):
    address1: str
    city: str
    state_code: str
    zip: str
    country_code: str


class Order(BaseModel):
    invoiceNumber: str
    email: str
    shippingAddress: ShippingAddress
    items: list[OrderItem]
    shippingRateUserDefinedId: str
