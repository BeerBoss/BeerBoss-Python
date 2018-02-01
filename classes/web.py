# Imports
import requests
import json
import os
from .display import Display

sysinfo = os.uname()
class Web:
    def __init__(self, webaddr, email, password):
        self.display = Display()
        self.webAddress = webaddr
        self.data = None
        self.auth = (email, password)
        self.osInfo = {'os': sysinfo.sysname, 'os_version': sysinfo.release, 'architecture': sysinfo.machine, 'hostname': sysinfo.nodename}

    def __del__(self):
        self.display.print("Web contact has been terminated!")

    def getDesiredTemp(self):
        if self.data:
            return self.data.desiredTemp
        else:
            return None

    def submitData(self, fridgeTemp, barrelTemp, coolerState, heaterState):
        if fridgeTemp is not None and barrelTemp is not None:
            data = {"tempData": {"fridgeTemp": round(fridgeTemp, 2), "barrelTemp": round(barrelTemp, 2), "cooler": coolerState, "heater": heaterState}, "connData": self.osInfo}
            try:
                data = json.loads(requests.post(self.webAddress + '/api/sensordata', json=data, auth=self.auth).text)
                if data:
                    self.data = data
                return 1
            except requests.ConnectionError as e:
                print("Request failed because I could not connect to the server")
                return 0
