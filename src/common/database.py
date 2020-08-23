import os

import pymongo


class Database(object):
    URI = os.environ.get("MONGOLAB_URI")
    DATABASE = None
    #URI = "mongodb://127.0.0.1:27017"


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()
        #Database.DATABASE = client.get_default_database()   Database.DATABASE = client['fullstack']




    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)