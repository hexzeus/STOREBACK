from fastapi import APIRouter
from app.services.printful import calculate_shipping_rates
from app.models.shipping import ShippingRequest

router = APIRouter()


@router.post("/")
async def calculate_shipping(shipping_request: ShippingRequest):
    rates = calculate_shipping_rates(shipping_request)
    if "error" in rates:
        return {"error": rates["error"]}
    return {"rates": rates}
