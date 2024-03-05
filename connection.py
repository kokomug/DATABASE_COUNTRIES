import json
import pymongo
import os
import sys
from random import randint

from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
CONNECTION_STRING = os.environ.get('PRIMARY_KEY')
client = MongoClient(CONNECTION_STRING)

# Database and collection
DATABASE_NAME = "countries_db"
COLLECTION_NAME = "countries"
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Load your JSON file
with open('countries.json', 'r') as file:
    data = json.load(file)

collection.insert_many(data)


print(f"Data imported into {DATABASE_NAME} database and {COLLECTION_NAME} collection.")