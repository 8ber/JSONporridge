import sys, os
import json

class Files_dal():
    def __init__(self):
        pass

    def get_all(self):
        with open(os.path.join(sys.path[0],"users.json"), "r") as file:
            data = json.load(file)
        return data

    def post_user(self, new_user):
        # alldata = self.get_all()
        # add_new_user = alldata["users"].append(new_user)
        with open(os.path.join(sys.path[0],"users.json"), "r") as file:
            data = json.load(file)
        
        data["users"].append(new_user)

        with open(os.path.join(sys.path[0],"users.json"), "w") as file:
            data = json.dump(data, file)


