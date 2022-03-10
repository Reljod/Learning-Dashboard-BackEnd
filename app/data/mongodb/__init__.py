from pymongo import MongoClient

from ...core.config import Config


def get_database():
    mongo_client = MongoClient(Config.DATABASE_URL)
    return mongo_client[Config.DATABASE_NAME]