from pymongo import MongoClient
import settings

class MongoDB:
    def __init__(self):
        self.__client=MongoClient(settings.MONGODB_URI, authSource='curso-python')
        self.__database = self.__client['curso-python']
    
    
    @classmethod
    def get_instance(cls):
        if not hasattr(cls, '__intance'):
            cls.__instance = cls()
        return cls.__instance
    
    
    def get_collection(self, collection_name):
        return self.get_database()[collection_name]
    
    
    def get_database(self):
        return self.__database