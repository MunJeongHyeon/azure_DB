import os
import sys
from random import randint

import pymongo
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.environ.get('COSMOS_CONNECTION_STRING')
DB_NAME = "products"
COLLECTION_NAME = "books"

client = pymongo.MongoClient(CONNECTION_STRING)

#데이터베이스

db = client[DB_NAME]
collection = db[COLLECTION_NAME]#컬렉션
'''
find_doc = collection.find_one({"category":"Marketing, Sales"})
print(find_doc)'''

find_docs = collection.find({"category":"Marketing, Sales"})
for doc in find_docs:
    print(doc)