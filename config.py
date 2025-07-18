import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # Read AUTH_USERS as a list of integers
    AUTH_USERS = list(map(int, os.getenv("AUTH_USERS", "").split()))
