import requests
from app.models.product import ProductModel, ProductVariant, ProductDetail
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Define the base URL for the Printful API
BASE_URL = "https://api.printful.com"

# Fetch API key and store ID from environment variables
API_KEY = os.getenv("PRINTFUL_API_KEY")
STORE_ID = os.getenv("PRINTFUL_STORE_ID")


def get_headers():
    """Helper function to get headers for the API request"""
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-PF-Store-Id": STORE_ID  # Add the store ID to the headers
    }


def get_product_details(product_id: str):
    """Fetch product details from Printful"""
    url = f"{BASE_URL}/products/{product_id}"
    headers = get_headers()
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["result"]["product"]

        product = ProductModel(
            id=data["id"],
            name=data["title"],
            description=data.get("description", ""),
            price=data.get("retail_price", 0),
            image_url=data.get("image", "")
        )

        variants = [
            ProductVariant(
                id=variant["id"],
                name=variant["title"],
                price=variant.get("retail_price", 0)
            )
            for variant in data.get("variants", [])
        ]

        return ProductDetail(product=product, variants=variants)
    else:
        return {"error": response.json().get("error", {}).get("message", "Unknown error")}


def create_printful_order(order_data):
    """Create an order in Printful"""
    url = f"{BASE_URL}/orders"
    headers = get_headers()
    response = requests.post(url, json=order_data.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()["result"]
    else:
        return {"error": response.json().get("error", {}).get("message", "Unknown error")}


def calculate_shipping_rates(shipping_request):
    """Calculate shipping rates in Printful"""
    url = f"{BASE_URL}/shipping/rates"
    headers = get_headers()
    response = requests.post(url, json=shipping_request.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()["result"]
    else:
        return {"error": response.json().get("error", {}).get("message", "Unknown error")}


def calculate_tax(tax_request):
    """Calculate tax estimates in Printful"""
    url = f"{BASE_URL}/orders/estimate-costs"
    headers = get_headers()
    response = requests.post(url, json=tax_request.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()["result"]["costs"]["vat"]
    else:
        return {"error": response.json().get("error", {}).get("message", "Unknown error")}
