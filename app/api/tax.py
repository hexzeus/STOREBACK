from fastapi import APIRouter
from app.services.printful import calculate_tax
from app.models.shipping import TaxRequest

router = APIRouter()


@router.post("/")
async def calculate_tax_endpoint(tax_request: TaxRequest):
    tax = await calculate_tax(tax_request)  # Await the coroutine
    if "error" in tax:
        return {"error": tax["error"]}
    return {"taxes": tax}
