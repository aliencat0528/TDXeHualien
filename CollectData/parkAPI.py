import requests
import json
import csv
import re
import math

from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint
#from tdxDemo.models import parkData


# import sys
# sys.path.append("C:\\herokuenv\\eHualien")
#
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eHualien.settings")
#
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

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
            ParkBaseData = json.loads(response)
            field="CarParkID,CarParkName,CarParkRegNo,OperatorID,Description,CarParkType,ParkingGuideType,ParkingTypes,ParkingSiteTypes,ChargeTypes,Telephone,EmergencyPhone,PositionLat,PositionLon,Email,Address,WebURL,SpecialOfferDescription,IsFreeParkingOutOfHours,VehicleRestriction,IsPublic,OperationType,LiveOccuppancyAvailable,EVRechargingAvailable,MonthlyTicketAvailable,SeasonTicketAvailable,ReservationAvailable,WheelchairAccessible,OvernightPermitted,TicketMachine,Toilet,Restaurant,Gas,Station,Shop,Gated,Lighting,SecureParking,TicketOffice,ProhibitedForAnyHazardousMaterialLoads,SecurityGuard,Supervision,LandMark,BuildingName,City,CityCode,FareDescription"
            # field = [
            #     "CarParkID",
            #     "CarParkName",
            #     "ParkingSiteTypes"
            # ]
            with open('ParkBase.csv', 'w', newline='',encoding="utf-8") as file:
                # for i in range(len(field)):
                #     file.write(field[i] + ",")
                #     if i + 1 == len(field):
                #         file.write("\r\n")

                # file.write(field)
                # print("stop")
                file.write(field)
                file.write("\n")
                for i in ParkBaseData['CarParks']:
                    # for x in field:
                    #     if x == "CarParkName":
                    #         file.writelines(i.get(x).get("Zh_tw") + ",")
                    #     elif x == "ParkingSiteTypes":
                    #         file.writelines(str(i.get(x)).replace("[", "").replace("]", "").replace(", ", ";") + ",")
                    #         temp = str(i.get(x)).replace("[", "").replace("]", "").replace(", ", ";")
                    #         temp = temp.split(";")
                    #         for j in temp:
                    #             print("value: " + j)
                    #     else:
                    #         file.writelines(str(i.get(x)) + ",")
                    # # file.writelines(str(i.get(field[i])) + ",")

                    for x in field.split(",")[:-1]:
                        if x=='CarParkName':
                            file.writelines(str(i.get(x).get("Zh_tw") + ","))
                        elif x=='PositionLat':
                            file.writelines(str(i.get('CarParkPosition').get('PositionLat'))+",")
                        elif x=='PositionLon':
                            file.writelines(str(i.get('CarParkPosition').get('PositionLon'))+",")
                        elif x =='ParkingTypes' or x=='ParkingSiteTypes' or x=='ChargeTypes':
                            file.writelines(str(i.get(x)).replace(",",";")+",")
                        # elif x=='FareDescription':
                        #     print(i.get(x))
                        #     #file.writelines(str(i.get(x).replace(" , ",";"))+",")
                        else:
                            file.writelines(str(i.get(x))+",")
                    file.write(str(i.get('FareDescription')))
                    file.write("\n")

                # for i in ParkBaseData['CarParks']:
                #     writer = csv.DictWriter(csvfile, fieldnames=i.keys())
                #     writer.writeheader()
                #     print(i)
                #     writer.writerow(i)
            # csvfile.close()


        elif(tag==1):
            ParkInfoData = json.loads(response)
            field="CarParkID,CarParkName,EntranceExitType,Entrances,Exits,EntranceExits"
            with open('ParkInfo.csv', 'w', newline='', encoding="utf-8") as file:
                file.write(field)
                file.write("\n")
                for i in ParkInfoData["ParkingEntranceExits"]:
                    for x in field.split(",")[:-1]:
                        file.writelines(str(i.get(x)) + ",")
                    file.write(str(i.get('EntranceExits')))
                    file.write("\n")
                # field = ParkInfoData["ParkingEntranceExits"][0].keys()
                # writer = csv.DictWriter(csvfile, fieldnames=field)
                # writer.writeheader()
                # for i in ParkInfoData["ParkingEntranceExits"]:
                #     writer.writerow(i)
            file.close()
        elif (tag==2):
            availParkData = json.loads(response)
            field="CarParkID,CarParkName,SpaceType,NumberOfSpaces,AvailableSpaces,ServiceStatus,FullStatus,ChargeStatus,DataCollectTime"
            with open('AvailPark.csv', 'w', newline='', encoding="utf-8") as file:
                file.write(field)
                file.write("\n")
                for i in availParkData["ParkingAvailabilities"]:
                    for x in field.split(",")[:-1]:
                        if x=='CarParkName':
                            file.writelines(str(i.get(x).get("Zh_tw") + ","))
                        elif x=='SpaceType':
                            file.write(str(i.get('Availabilities')[0].get('SpaceType'))+ ",")
                        elif x=='NumberOfSpaces':
                            file.write(str(i.get('Availabilities')[0].get('NumberOfSpaces')) + ",")
                        elif x=='AvailableSpaces':
                            file.write(str(i.get('Availabilities')[0].get('AvailableSpaces')) + ",")
                        else:
                            file.writelines(str(i.get(x)) + ",")
                    file.write(str(i.get('DataCollectTime')))
                    file.write("\n")
                # field = availParkData["ParkingAvailabilities"][0].keys()
                # writer = csv.DictWriter(csvfile, fieldnames=field)
                # writer.writeheader()
                # for i in availParkData["ParkingAvailabilities"]:
                #     writer.writerow(i)
            file.close()
        else:
            pass

    def parkInfo(self,kind):
        if kind=="parkavailable":
            mergepark =""
            with open('AvailPark.csv', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for r in reader:
                    mergepark+=("{}:{}".format(str(r['CarParkName']),str(r['AvailableSpaces']))+"\n")

                    # #linepark = dict(zip([(dict(eval(r['CarParkName'])).values())], [r['AvailableSpaces']]))
                    # linepark = (r['CarParkName'].split(": '")[1].rstrip("'}"), r['AvailableSpaces'])
                    # mergepark.append(linepark)
                    # #print(linepark)
            csvfile.close()
            print(mergepark)
            return mergepark
        else:
            pass



class DealLoc():

    def __init__(self,usrLat, usrLon):
        self.usrLat = usrLat
        self.usrLon = usrLon

    def cntDistance(self):
        allEE= self.getParkLoc()
        ra = 6378140  # 赤道半徑
        rb = 6356755  # 極半徑
        flatten = (ra - rb) / ra  # Partial rate of the earth
        # change angle to radians
        radLatA = math.radians(self.usrLat)
        radLonA = math.radians(self.usrLon)
        for a in allEE:
            radLatB = math.radians(float(a.get('PositionLat')))
            radLonB = math.radians(float(a.get('PositionLon')))

            pA = math.atan(rb / ra * math.tan(radLatA))
            pB = math.atan(rb / ra * math.tan(radLatB))
            x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
            c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
            c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
            dr = flatten / 8 * (c1 - c2)
            distance = ra * (x + dr)
            distance = round(distance / 1000, 4)
            #print(f'{distance} km')
            a['distance']=distance
        return allEE



    def getParkLoc(self):
        #newdata=[]
        eachdict=[]
        global locAdd
        with open('ParkBase.csv', encoding="utf-8") as file:
            info=file.read()
            eachPark=[j for j in [i.split("\n") for i in info.split("\n")[:-1]]]
            key=[] #eachPark[0] --- len:1
            value=[]  #eachPark[1:] --- len:47
            for k in eachPark[0]:
                key=k.split(",")
            for v in eachPark[1:]:
                for ev in v:
                    #print(ev)
                    # valueRule=re.compile(r'\[(\d*$[, \d*])\]')#[1,2,3,4],[254] fail :(
                    # testrlt=valueRule.findall(ev)
                    # print(testrlt)
                    value=ev.split(",")
                    locAdd=dict(zip(key,value))
                    eachdict.append(locAdd)
            #newdata.append(eachdict)
            # for k in key:
            #     print(len(k.split(",")))  #len:47
            # for v in value:
            #     for vv in v:
            #         print(len(vv.split(","))) #49/51/48/51/50/48/48/48/53/55/47/51/57/47/49/57/47/47/48/47/48/53/48/48/47/49/47/49/58/51/48/49/54/51/48/52/49/48/52/50/49/51/47/47/57/47/49

            # for pd in range(len(eachPark[0])):
            #     print(type(eachPark[0][pd]),eachPark[1:][pd])
            #locAdd=dict(zip([eachPark[0][pd]],eachPark[1:][pd]))
        #print(eachdict)
        return eachdict

    def getNearInfo(self,toSort):
        #print(toSort)
        topfive=""
        parkSort=sorted(toSort,key=lambda x:x.get('distance'))
            #print(ts.get('distance'))
        for newpark in parkSort[:4]:
            print(newpark)
            topfive+="{}\n>>>收費:{}".format(newpark['CarParkName'],newpark['FareDescription']+"\n"+"\n")
        topfive += "{}\n>>>收費:{}".format(newpark['CarParkName'], newpark['FareDescription'] + "\n")
        return  topfive

    # def getLocOldVer(self):
    #     global stations, lat, lng, parkname
    #     stations = {};
    #     lat = [];
    #     lng = [];
    #     parkname = [];
    #     with open('ParkInfo.csv', encoding="utf-8") as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for r in reader:
    #             # print(r["EntranceExitType"])
    #             if r["EntranceExitType"] == str(1):
    #                 # print("*****")
    #                 parkname.append(r['CarParkName'])
    #                 loc = eval(r['EntranceExits'])
    #
    #                 if (len(loc) > 1):
    #                     # print(loc[:1][0]["Position"]["PositionLat"])
    #                     lat.append(loc[:1][0]["Position"]["PositionLat"])
    #                     lng.append(loc[:1][0]["Position"]["PositionLon"])
    #                 else:
    #                     for k in loc:
    #                         # print(k["Position"]["PositionLat"])
    #                         lat.append(k["Position"]["PositionLat"])
    #                         lng.append(k["Position"]["PositionLon"])
    #
    #             else:
    #                 parkname.append(r['CarParkName'])
    #                 con = eval(r['Entrances'])
    #                 if (len(con) > 1):
    #                     # print(loc[:1][0]["Position"]["PositionLat"])
    #                     lat.append(con[:1][0]["Position"]["PositionLat"])
    #                     lng.append(con[:1][0]["Position"]["PositionLon"])
    #                 else:
    #                     for c in con:
    #                         # print(c['Position']['PositionLat'])
    #                         lat.append(c["Position"]["PositionLat"])
    #                         lng.append(c["Position"]["PositionLon"])
    #
    #                     # print(c['Position'])
    #                 # print("-------")
    #             # r["Entrances"]
    #
    #         csvfile.close()
    #     stations['latitude'] = lat
    #     stations['logtitude'] = lng
    #     stations['parkN'] = parkname
    #     return stations

    # def getCntDistOldVer(self):
    #     allEE = self.getParkEntranceExitLoc()
    #     print(allEE)
    #     global dist, parkLat, parkLon
    #     dist = [];
    #     parkLat = 0.0;
    #     parkLon = 0.0
    #     ra = 6378140  # 赤道半徑
    #     rb = 6356755  # 極半徑
    #     flatten = (ra - rb) / ra  # Partial rate of the earth
    #     # change angle to radians
    #     radLatA = math.radians(self.usrLat)
    #     radLonA = math.radians(self.usrLon)
    #     Lat = allEE['latitude']
    #     Lon = allEE['logtitude']
    #
    #     for v in range(len(Lat)):
    #         parkLat = Lat[v]
    #         parkLon = Lon[v]
    #         # print(Lat[v], Lon[v])
    #         radLatB = math.radians(parkLat)
    #         radLonB = math.radians(parkLon)
    #
    #         pA = math.atan(rb / ra * math.tan(radLatA))
    #         pB = math.atan(rb / ra * math.tan(radLatB))
    #         x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    #         c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    #         c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    #         dr = flatten / 8 * (c1 - c2)
    #         distance = ra * (x + dr)
    #         distance = round(distance / 1000, 4)
    #         dist.append(distance)
    #         # print(f'{distance}km')
    #         allEE['distance'] = dist
    #     # sortrlt=sorted(allEE['distance'])
    #     #
    #     # self.getNearInfo(allEE,sortrlt)
    #     # return dist

if __name__ == '__main__':
    nearinfo=DealLoc(25.030094, 121.557377)
    rlt=nearinfo.cntDistance()
    print(nearinfo.getNearInfo(rlt))

    # data = DealData(
    #     ['https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/CarPark/City/HualienCounty?%24format=JSON',
    #      'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
    #      'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON']
    #
    # )
    # data.getData()
    # print(data)
    # data.parkInfo("parkavailable")





