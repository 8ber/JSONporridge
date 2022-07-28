import requests


class API_dal:
    def __init__(self):
        pass
 
    def get_all(self):
        resp = requests.get("https://jsonplaceholder.typicode.com/users")
        return resp.json()

    def post_user(self, new_user):
        resp = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
        print(resp.json())
