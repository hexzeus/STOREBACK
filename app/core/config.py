import os


class Settings:
    app_name = "Merch Backend"
    admin_email = os.getenv("ADMIN_EMAIL")
    printful_api_key = os.getenv("PRINTFUL_API_KEY")
    printful_store_id = os.getenv("PRINTFUL_STORE_ID")
    stripe_secret_key = os.getenv("STRIPE_SECRET_KEY")
    next_public_stripe_public_key = os.getenv("NEXT_PUBLIC_STRIPE_PUBLIC_KEY")
    next_public_base_url = os.getenv("NEXT_PUBLIC_BASE_URL")


settings = Settings()
