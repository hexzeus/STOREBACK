from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import products, orders, shipping, tax

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
