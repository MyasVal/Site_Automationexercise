import requests


class CreateAccountAPI:
    def __init__(self):
        self.url = "https://automationexercise.com/api/createAccount"

    def create_account(self, data):
        response = requests.post(self.url, json=data)
        return response
