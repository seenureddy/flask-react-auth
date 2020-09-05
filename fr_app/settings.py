import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/fra")
DB_NAME = os.getenv("MONGODB_NAME", "fra")

class Config:
    MONGODB_SETTINGS = {
        'host': MONGODB_URI,
        'db': DB_NAME,
        'connect': False,
    }

