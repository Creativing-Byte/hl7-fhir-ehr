from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb://JuanGuzman:Hola123@sampleinformationservic-shard-00-00.x31xs.mongodb.net:27017,sampleinformationservic-shard-00-01.x31xs.mongodb.net:27017,sampleinformationservic-shard-00-02.x31xs.mongodb.net:27017/?replicaSet=atlas-pdxqbo-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=SampleinformationService"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
