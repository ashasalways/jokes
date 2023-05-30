import requests

import datetime

class Jokehandler:

    def __init__(self, address):
        self.address = address
        nu = datetime.datetime.now()
        print(f"konstruktor körs tid: {nu}")

    def getJoke(self):
        req = requests.get(self.address)
        jsonData = req.json()

        joke = jsonData['joke']

        #nu = datetime.datetime.now()
        #print(f"metod körs tid: {nu}")

        return joke