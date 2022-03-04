import requests
import json
import csv
import math

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
        #print(len(self.url))
        for u in range(len(self.url)):
            #print(self.url[u],u)
            response = request('get', self.url[u],
                               headers=a.get_auth_header())
            #print(response)
            self.saveData(response.text,u)


    def saveData(self,response,tag):
        if(tag==0):
            ParkInfoData = json.loads(response)
            with open('ParkInfo.csv', 'w', newline='',encoding="utf-8") as csvfile:
                field = ParkInfoData["ParkingEntranceExits"][0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=field)
                writer.writeheader()
                for i in ParkInfoData["ParkingEntranceExits"]:
                    writer.writerow(i)
                csvfile.close()


        elif(tag==1):
            availParkData = json.loads(response)
            with open('AvailPark.csv', 'w', newline='', encoding="utf-8") as csvfile:
                field = availParkData["ParkingAvailabilities"][0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=field)
                writer.writeheader()
                for i in availParkData["ParkingAvailabilities"]:
                    writer.writerow(i)

            csvfile.close()
        else:
            pass
    def parkInfo(self,kind):
        if kind=="parkavailable":
            mergepark = []
            with open('AvailPark.csv', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for r in reader:
                    linepark = dict(zip([(dict(eval(r['CarParkName'])).values())], [r['AvailableSpaces']]))
                    mergepark.append(linepark)
                    # print(linepark)
            csvfile.close()
            print(str(mergepark))
            return mergepark
        else:
            pass



class DealLoc():

    def __init__(self,usrLat, usrLon):
        self.usrLat = usrLat
        self.usrLon = usrLon

    def cntDistance(self):
        allEE= self.getParkLoc()
        print(allEE)
        global dist,parkLat,parkLon
        dist=[]; parkLat=0.0;parkLon=0.0
        ra = 6378140  # 赤道半徑
        rb = 6356755  # 極半徑
        flatten = (ra - rb) / ra  # Partial rate of the earth
        # change angle to radians
        radLatA = math.radians(self.usrLat)
        radLonA = math.radians(self.usrLon)
        Lat=allEE['latitude']
        Lon=allEE['logtitude']

        for v in range(len(Lat)):
            parkLat=Lat[v]
            parkLon=Lon[v]
            #print(Lat[v], Lon[v])
            radLatB = math.radians(parkLat)
            radLonB = math.radians(parkLon)

            pA = math.atan(rb / ra * math.tan(radLatA))
            pB = math.atan(rb / ra * math.tan(radLatB))
            x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
            c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
            c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
            dr = flatten / 8 * (c1 - c2)
            distance = ra * (x + dr)
            distance = round(distance / 1000, 4)
            dist.append(distance)
            #print(f'{distance}km')
            allEE['distance']=dist
        return dist

    def getParkLoc(self):
        global stations, lat, lng, parkname
        stations = {};
        lat = [];lng = [];parkname = [];
        with open('ParkInfo.csv',encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for r in reader:
                # print(r["EntranceExitType"])
                if r["EntranceExitType"] == str(1):
                    # print("*****")
                    parkname.append(r['CarParkName'])
                    loc = eval(r['EntranceExits'])

                    if (len(loc) > 1):
                        # print(loc[:1][0]["Position"]["PositionLat"])
                        lat.append(loc[:1][0]["Position"]["PositionLat"])
                        lng.append(loc[:1][0]["Position"]["PositionLon"])
                    else:
                        for k in loc:
                            # print(k["Position"]["PositionLat"])
                            lat.append(k["Position"]["PositionLat"])
                            lng.append(k["Position"]["PositionLon"])

                else:
                    parkname.append(r['CarParkName'])
                    con = eval(r['Entrances'])
                    if (len(con) > 1):
                        # print(loc[:1][0]["Position"]["PositionLat"])
                        lat.append(con[:1][0]["Position"]["PositionLat"])
                        lng.append(con[:1][0]["Position"]["PositionLon"])
                    else:
                        for c in con:
                            # print(c['Position']['PositionLat'])
                            lat.append(c["Position"]["PositionLat"])
                            lng.append(c["Position"]["PositionLon"])

                        # print(c['Position'])
                    # print("-------")
                # r["Entrances"]

            csvfile.close()
        stations['latitude'] = lat
        stations['logtitude'] = lng
        stations['parkN'] = parkname


        return stations

    def getNearInfo(self):
        return
if __name__ == '__main__':
    nearinfo=DealLoc(25.030094, 121.557377)
    rlt=nearinfo.cntDistance()
    print(rlt)
#     data=DealData(['https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
#             'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON'])
#
#     data.getData()
#     print(data)
#     data.parkInfo("parkavailable")





