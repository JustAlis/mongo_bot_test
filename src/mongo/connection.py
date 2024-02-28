from motor.motor_asyncio import AsyncIOMotorClient
from config import conf

client = AsyncIOMotorClient(conf.mongo_connection_str)
database = client[conf.mongo_database]
collection = database[conf.mongo_collection]
