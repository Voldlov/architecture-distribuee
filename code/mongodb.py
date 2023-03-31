import os
from pymongo import MongoClient

class MongoBDD():
        def __init__(self) -> None:
            self.MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
            self.MONGODB_ATLAS_PASSWORD = os.getenv("MONGODB_ATLAS_PASSWORD")
            self.MONGODB_ATLAS_URI = "mongodb+srv://{}:{}@cluster0.6jprsq1.mongodb.net/".format(self.MONGODB_ATLAS_USER, self.MONGODB_ATLAS_PASSWORD)
            self.MONGO_DB_NAME = os.getenv("MONGODB_ATLAS_DATABASE")

            self.pymongo_client = MongoClient(self.MONGODB_ATLAS_URI)
            pass

