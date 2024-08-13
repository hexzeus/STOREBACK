from fastapi import APIRouter
from app.services.printful import create_printful_order
from app.models.order import Order

router = APIRouter()


@router.post("/")
async def create_order(order: Order):
    order_response = create_printful_order(order)
    if "error" in order_response:
        return {"error": order_response["error"]}
    return order_response
