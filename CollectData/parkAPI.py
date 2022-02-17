import requests
import json
import csv

from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint

app_id = 'NQAwADEAZgAxADIAYQAwAC0AZQA0AGEAZAAtADQANgA1ADYALQA4ADUAMQAwAC0AYgBmAGYANQA4ADIANQAxADQAMgBiAGYA'
app_key = 'OQA0ADIAMwBhADQANQBmAC0AMABjAGYAZgAtADQAMQAyADMALQBiAGEAMAA4AC0AZQA1ADIAOQA0ADAAZgA5ADMAOABhADIA'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }

class DealData():
    def __init__(self,url):
        self.url = url


    def getData(self):
        a = Auth(app_id, app_key)
        response = request('get',self.url,
                 headers=a.get_auth_header())
        self.saveData(response.text)
    def saveData(self,response):
        availParkData = json.loads(response)
        with open('AvailPark.csv', 'w', newline='',encoding="utf-8") as csvfile:
            field = availParkData["ParkingAvailabilities"][0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=field)
            writer.writeheader()
            for i in availParkData["ParkingAvailabilities"]:
                writer.writerow(i)

            csvfile.close()

    def showInfo(self):
        mergepark=[]
        with open('AvailPark.csv', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for r in reader:
                    linepark=dict(zip([(dict(eval(r['CarParkName'])).values())],[r['AvailableSpaces']]))
                    mergepark.append(linepark)
                    #print(linepark)
        csvfile.close()
        #print(mergepark)
        return mergepark
# if __name__ == '__main__':
#     data=DealData('https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON')
#     #data.getData()
#     data.showInfo()





