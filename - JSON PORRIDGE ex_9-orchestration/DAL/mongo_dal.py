from pymongo import MongoClient

class Mongo_dal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["usersDB"]


    def get_all(self):
        response = self.__db["users"].find({})
        arr = []
        for user in response:
            arr.append(user)
        return arr 

    def post_user(self, new_user):
        self.__db["users"].insert_one(new_user)