from pymongo import MongoClient
# from bson.objectid import ObjectId
from bson import ObjectId
MongoDbUri="mongodb+srv://bhumikakatta20:BhumikaSharanRishav@cluster0.6yh3f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client=MongoClient(MongoDbUri)

db=client.expense

def addOneRecord(record):
    ItemsCol=db.spenton
    result=ItemsCol.insert_one(record)
    print("Record has been added")
    return

# for db_name in client.list_database_names():
#     print(db_name)

ItemsCol=db.spenton
cursor=ItemsCol.find()
# print(a)
print(type(cursor))
for record in cursor:
        print(record)
# record={'Date': '2024-10-01', 'Category': 'Baby', 'SpentOn': 'baby', 'Amount': 235.0}
# record={"Category": "aaby",   "SpentOn": "aaby",   "Amount": 25.0}
# record={"Name":"Pen","Email":"Bhumi@gmail.com","Quantity":4}
# ItemsCol.insert_one(record)