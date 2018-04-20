from observer import Observable
import json

class LoginModel():

    def __init__(self):
        self.user = {}
        self.load_user()

    def load_user(self):
        with open('models/database/user.json', 'r') as f:
            json_str = json.load(f)
            for id, info in json_str.items():
                self.user[id] = info

    def add_user(self):
        pass

    def remove_user(self):
        pass

    def verify_user(self, id, password):
        if id in self.user:
            if self.user[id]['password'] == password:
                return self.user[id]
        return False

