from pymongo import MongoClient
from config import conf

client = MongoClient(conf.mongo_connection_str)
database = client[conf.mongo_database]
collection = database[conf.mongo_collection]
