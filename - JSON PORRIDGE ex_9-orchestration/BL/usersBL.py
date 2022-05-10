#importing modules + relevant DALs
from DAL.API_dal import *
from DAL.files_dal import *
from DAL.mongo_dal import *
 
class usersBL:
    def __init__(self):
        self.__API_dal = API_dal()  #The id, name & email 
        self.__files_dal = Files_dal()  #mobile phone
        self.__mongo_dal = Mongo_dal()  #address - city,country EXTERNAL ID

    def get_all(self):
        api_data = self.__API_dal.get_all()
        files_data = self.__files_dal.get_all()
        db_data = self.__mongo_dal.get_all()

        arr = []
        #data from file
        for person in files_data["users"]:
            obj = {}
            obj["phone"] = person["phone"]
            obj["id"] = person["id"]
           
        #data from API
            dat = list(filter(lambda x: x["id"] == person["id"], api_data))
            for person in dat:
                if len(dat) > 0:
                    obj["name"] = person["name"]
                    obj["email"] = person["email"]
        
        #data from mongoDB
            db_user = []
            db_user = list(filter(lambda x: x["externalid"] == int(person["id"]),db_data))
            if len(db_user) > 0:
                obj["address"] = {}
                obj["address"]["city"] = db_user[0]["city"]
                obj["address"]["country"]= db_user[0]["country"]

            arr.append(obj)
        return arr

    def post_user(self, new_user):
        id = len(self.__files_dal.get_all()["users"]) + 1
        #destructuring the JSON from the client ---> to API 
        print(f"------------{id}-----------")
        data_to_API = {"name": new_user["name"], "email": new_user["email"]}
        self.__API_dal.post_user(data_to_API)

        #destructuring the JSON from the client ---> to a system file
        phone = { "id" : id, "phone" : new_user["phone"] }
        self.__files_dal.post_user(phone)

        # #destructuring the JSON from the client ---> to MongoDB
        data_to_DB = {"city" : new_user["city"], "country" : new_user["country"], "externalid" : id}
        self.__mongo_dal.post_user(data_to_DB)
