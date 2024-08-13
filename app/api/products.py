from fastapi import APIRouter
from app.services.printful import get_product_details

router = APIRouter()


@router.get("/{product_id}")
async def get_product(product_id: str):
    product_details = get_product_details(product_id)
    if "error" in product_details:
        return {"error": product_details["error"]}
    return product_details
