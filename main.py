from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.api import products, orders, shipping, tax

# Load environment variables from .env file
load_dotenv()

# Access the Printful API key
api_key = os.getenv("PRINTFUL_API_KEY")

app = FastAPI()

# Register API routes
app.include_router(products.router, prefix="/api/products")
app.include_router(orders.router, prefix="/api/orders")
app.include_router(shipping.router, prefix="/api/shipping")
app.include_router(tax.router, prefix="/api/tax")


@app.get("/")
def read_root():
    return {
        "message": "Your custom server welcome message",
        "status": "Server is up and running!"
    }
