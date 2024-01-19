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
books = [
    {
        "_id":1,
        "category":"Marketing, Sales",
        "name":"마케팅 불변의 법칙",
        "author":"알 리스, 잭 트라우트",
        "publisher":"비즈니스"
    },
    {
        "_id":2,
        "category":"Marketing, Sales",
        "name":"정상에서 만납시다",
        "author":"지그지글러",
        "quantiy":1
    }
]
result = collection.insert_many(books)