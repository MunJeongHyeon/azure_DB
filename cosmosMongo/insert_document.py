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
book = {
    "category":"Computers, Technology",
    "name":"MonogoDB The Definitive Guide",
    "quantiy":2,
    "sale":False
},
result = collection.insert_many(book)
print("추가된 문서 _id:{}.\n".format(result.inserted_ids[0]))