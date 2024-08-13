from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# Define allowed origins
allowed_origins = [
    "https://storeback-jexl.onrender.com",  # Your deployed backend URL
    "http://localhost:3000",  # Your local development frontend URL
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Allows only specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define the Printful API base URL
BASE_URL = "https://api.printful.com"

# Fetch API key and store ID from environment variables
PRINTFUL_API_KEY = os.getenv("PRINTFUL_API_KEY")
PRINTFUL_STORE_ID = os.getenv("PRINTFUL_STORE_ID")


# Helper function to create headers for API requests
def get_headers():
    return {
        "Authorization": f"Bearer {PRINTFUL_API_KEY}",
        "X-PF-Store-Id": PRINTFUL_STORE_ID,
        "Content-Type": "application/json"
    }


@app.get("/api/products")
def get_products():
    """Fetch products from the Printful API"""
    url = f"{BASE_URL}/store/products"  # Using the base URL defined above
    headers = get_headers()
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["result"]
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/")
def read_root():
    return {
        "message": "Your custom server welcome message",
        "status": "Server is up and running!"
    }
