from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MONGO_PASSWORD =  getenv("MONGO_PASS")
MONGO_USERNAME =  getenv("MONGO_USER")
MONGO_DBNAME =  getenv("MONGO_DB")
URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.qjwqn.mongodb.net/{MONGO_DBNAME}?retryWrites=true&w=majority"

client = MongoClient(URI)
DB = client.ADMIN   
ADMIN = DB.ADMIN    
USERS = DB.USERS    
