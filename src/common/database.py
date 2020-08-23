import os

import pymongo


class Database(object):
    #URI = os.environ.get("MONGOLAB_URI")
    DATABASE = None
    URI="mongodb://<fanzhou>:<fanzhou3>@ds041561.mlab.com:41561/heroku_g3q7pzwj"
    #URI = "mongodb://127.0.0.1:27017"


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['heroku_g3q7pzwj']
        #Database.DATABASE = client.get_default_database()    client['fullstack']  client['heroku_g3q7pzwj']




    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)