import pymongo 
from os import getenv
from dotenv import load_dotenv

load_dotenv()

MONGO_PASSWORD =  getenv("MONGO_PASS")
MONGO_USERNAME =  getenv("MONGO_USER")
MONGO_DBNAME =  getenv("MONGO_DB")
URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.cuwcn.mongodb.net/{MONGO_DBNAME}?retryWrites=true&w=majority"
print(URI)
client = pymongo.MongoClient(URI)
DB = client.data_base   
ADMIN = DB.ADMIN    
USERS = DB.USERS    

#for i in USERS.find(): USERS.delete_one({"_id":i["_id"]})
for i in USERS.find(): print(i)
#for i in ADMIN.find(): ADMIN.delete_one({"_id":i["_id"]})
for i in ADMIN.find(): print(i)