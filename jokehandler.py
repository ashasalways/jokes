import requests

class Jokehandler:

    def __init__(self, address):
        self.address = address

    def getJoke(self):
        req = requests.get(self.address)
        jsonData = req.json()
        joke = jsonData['joke']