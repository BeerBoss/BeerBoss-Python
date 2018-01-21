# Imports
import requests
import json
from .lcd import Lcd

class Web:
    def __init__(self, webaddr, email, password):
        self.lcd = Lcd()
        self.webAddress = webaddr
        self.data = None
        self.auth = (email, password)

    def __del__(self):
        self.lcd.print("Web contact has been terminated!")


    def getData(self):
        request = requests.get(self.webAddress)
        self.data = json.loads(request.json())

    def submitData(self, fridgeTemp, barrelTemp, coolerState, heaterState):
        if fridgeTemp is not None and barrelTemp is not None:
            data = {"fridgeTemp": fridgeTemp, "barrelTemp": barrelTemp, "cooler": coolerState, "heater": heaterState}
            try:
                r= requests.post(self.webAddress + '/api/sensordata', json=data, auth=self.auth)
                print(r.content)
            except (requests.ConnectionError) as e:
                print(e)
