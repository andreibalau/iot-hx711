import requests
import json

PARKINGPAL_API_URL = "http://localhost:8080/availability"
class SensorService:
    def __init__(self):
        self.latitude=45.608141
        self.longitude=25.303963
        self.availability=None
        
    def notifyServer(self):
        serviceData = {
                "latitude":self.latitude,
                "longitude":self.longitude,
                "availability":self.availability
            }
        print("data sent =>",serviceData)
        data=requests.post(url=PARKINGPAL_API_URL,json=serviceData)
        print("status code:",data.status_code)
        
    def checkAvailability(self,weight):
        if weight<=20:
            print("less than 20g,free spot")
            self.availability = True
        else:
            print("higher than 20g, busy spot")
            self.availability = False
          