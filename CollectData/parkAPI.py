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



# import sys
# sys.path.append("C:\\herokuenv\\eHualien")
#
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eHualien.settings")
import django
django.setup()
from tdxDemo.models import parkInfoDB
from django.db.models import *
from django.db.models.functions import *




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
            #print("response::",response)
            self.saveData(response.text,u)


    def saveData(self,response,tag):
        if(tag==0):
            ParkBaseData = json.loads(response)
            field="CarParkID,CarParkName,CarParkRegNo,OperatorID,Description,CarParkType,ParkingGuideType,ParkingTypes,ParkingSiteTypes,ChargeTypes,Telephone,EmergencyPhone,PositionLat,PositionLon,Email,Address,WebURL,SpecialOfferDescription,IsFreeParkingOutOfHours,VehicleRestriction,IsPublic,OperationType,LiveOccuppancyAvailable,EVRechargingAvailable,MonthlyTicketAvailable,SeasonTicketAvailable,ReservationAvailable,WheelchairAccessible,OvernightPermitted,TicketMachine,Toilet,Restaurant,GasStation,Shop,Gated,Lighting,SecureParking,TicketOffice,ProhibitedForAnyHazardousMaterialLoads,SecurityGuard,Supervision,LandMark,BuildingName,City,CityCode,FareDescription"
            with open('ParkBase.csv', 'w', newline='',encoding="utf-8") as file:
                file.write(field)
                file.write("\n")
                for i in ParkBaseData['CarParks']:
                    for x in field.split(",")[:-1]:
                        if x=='CarParkName':
                            file.writelines(str(i.get(x).get("Zh_tw") + ","))
                        elif x=='PositionLat':
                            file.writelines(str(i.get('CarParkPosition').get('PositionLat'))+",")
                        elif x=='PositionLon':
                            file.writelines(str(i.get('CarParkPosition').get('PositionLon'))+",")
                        elif x =='ParkingTypes' or x=='ParkingSiteTypes' or x=='ChargeTypes':
                            file.writelines(str(i.get(x)).replace(",",";")+",")
                        elif x=='SpecialOfferDescription' or x=='VehicleRestriction':
                            file.writelines(str(i.get(x)).replace(",", ";") + ",")
                        else:
                            file.writelines(str(i.get(x))+",")
                    file.write(str(i.get('FareDescription')))
                    file.write("\n")



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
            csvfile.close()
            #print(mergepark)
            return mergepark
        else:
            pass



class DealLoc():

    def __init__(self,*args):
        if args:
            self.usrLat = args[0]
            self.usrLon = args[1]

    def cntDistance(self):
        allEE = parkInfoDB.objects.annotate(distance=6371 * ACos(
            Cos(Radians(self.usrLat))
            * Cos(Radians('PositionLat'))
            * Cos(Radians('PositionLon') - Radians(self.usrLon))
            + Sin(Radians(self.usrLat))
            * Sin(Radians('PositionLat'))
            , output_field=FloatField())).order_by('distance')

        return allEE.values()

    def getParkLoc(self):
        getDB=DealToDB()
        dbinfo=getDB.passValue('all')
        return dbinfo

    def getNearInfo(self,parkdata,cond):
        parkSort=parkdata[:cond]
        topfive = ""
        locAdd = {}
        global i
        i = 0
        for newpark in parkSort[:cond-1]:
            locAdd[i]=[newpark['CarParkName'], newpark['PositionLat'], newpark['PositionLon']]
            topfive+="{}\n>>>收費:{}".format(newpark['CarParkName'],newpark['FareDescription']+"\n"+"\n")
            i+=1
        locAdd[i] = [parkSort[cond-1]['CarParkName'], parkSort[cond-1]['PositionLat'], parkSort[cond-1]['PositionLon']]
        topfive += "{}\n>>>收費:{}".format(parkSort[cond-1]['CarParkName'], parkSort[cond-1]['FareDescription'] + "\n")
        #print(locAdd)
        return topfive,locAdd,parkdata


class DealToDB():

    def toDB(self):
        with open('ParkSort.csv', encoding="utf-8") as file:
            sortData = file.read()
            sortData = eval(sortData)
            eachsd = [sd for sd in sortData]
            for esd in eachsd:
                db=parkInfoDB.objects.create(CarParkID=esd.get('CarParkID'),CarParkName=esd.get('CarParkName'),CarParkRegNo=esd.get('CarParkRegNo'),OperatorID=esd.get('OperatorID'),Description=esd.get('Description'),CarParkType=esd.get('CarParkType'),ParkingGuideType=esd.get('ParkingGuideType'),ParkingTypes=esd.get('ParkingTypes'),ParkingSiteTypes=esd.get('ParkingSiteTypes'),ChargeTypes=esd.get('ChargeTypes'),Telephone=esd.get('Telephone'),EmergencyPhone=esd.get('EmergencyPhone'),PositionLat=esd.get('PositionLat'),PositionLon=esd.get('PositionLon'),Email=esd.get('Email'),Address=esd.get('Address'),WebURL=esd.get('WebURL'),FareDescription=esd.get('FareDescription'),SpecialOfferDescription=esd.get('SpecialOfferDescription'),IsFreeParkingOutOfHours=esd.get('IsFreeParkingOutOfHours'),VehicleRestriction=esd.get('VehicleRestriction'),IsPublic=esd.get('IsPublic'),OperationType=esd.get('OperationType'),LiveOccuppancyAvailable=esd.get('LiveOccuppancyAvailable'),EVRechargingAvailable=esd.get('EVRechargingAvailable'),MonthlyTicketAvailable=esd.get('MonthlyTicketAvailable'),SeasonTicketAvailable=esd.get('SeasonTicketAvailable'),ReservationAvailable=esd.get('ReservationAvailable'),WheelchairAccessible=esd.get('WheelchairAccessible'),OvernightPermitted=esd.get('OvernightPermitted'),TicketMachine=esd.get('TicketMachine'),Toilet=esd.get('Toilet'),Restaurant=esd.get('Restaurant'),GasStation=esd.get('GasStation'),Shop=esd.get('Shop'),Gated=esd.get('Gated'),Lighting=esd.get('Lighting'),SecureParking=esd.get('SecureParking'),TicketOffice=esd.get('TicketOffice'),ProhibitedForAnyHazardousMaterialLoads=esd.get('ProhibitedForAnyHazardousMaterialLoads'),SecurityGuard=esd.get('SecurityGuard'),Supervision=esd.get('Supervision'),LandMark=esd.get('LandMark'),BuildingName=esd.get('BuildingName'),City=esd.get('City'),CityCode=esd.get('CityCode'))
                db.save()
                print('**save:{}**'.format(esd.get('CarParkID')))
        print('---save---')

    # def __init__(self):
    #     self.allinfo=parkInfoDB.objects.all().values()

    def passValue(self,*field,**action):
        allinfo=parkInfoDB.objects.all().values()
        #print(allinfo)
        if action:
            pass
        else:
            contf = [] ; mulfield=[]
            for ai in allinfo:
                if (len(field) > 1):
                    eachf=[]
                    for f in field:
                        eachf.append(ai.get(f))
                    contf.append({ai.get('CarParkID'): eachf})
                    mulfield.append(eachf)
                else:
                    if (field[0] == 'all'):
                        return list(allinfo)
                    else:
                        mulfield.append(ai.get(field))
                        contf.append({ai.get('CarParkID'): mulfield})
            return contf

        #option1
        # testmp=parkInfoDB.objects.all()
        # for tm in testmp.values():  ##dict
        #     print(tm.get('PositionLat'),tm.get('PositionLon'))

        #option2
        # sqltest = parkInfoDB.objects.raw('SELECT CarParkID, PositionLat ,PositionLon FROM tdxDemo_parkinfodb')
        # print(sqltest)
        # print(len(sqltest))
        # for st in sqltest:
        #     print(st.PositionLat, st.PositionLon)

        # print('------function test---------')
        # print(parkInfoDB.objects.get(CarParkName='花蓮民生停車場'))##parkInfoDB object (A00033)
        # print(parkInfoDB.objects.filter(CarParkName='花蓮民生停車場'))##<QuerySet [<parkInfoDB: parkInfoDB object (A00033)>]>




if __name__ == '__main__':
    # data = DealData(
    #     ['https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/CarPark/City/HualienCounty?%24format=JSON',
    #      'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingEntranceExit/City/HualienCounty?%24format=JSON',
    #      'https://traffic.transportdata.tw/MOTC/v1/Parking/OffStreet/ParkingAvailability/City/HualienCounty?%24format=JSON']
    #
    # )
    # data.getData()
    # print(data)
    # data.parkInfo("parkavailable")
    #
    nearinfo = DealLoc(25.030094, 121.557377)
    rlt = nearinfo.cntDistance()
    print(nearinfo.getNearInfo(rlt,5)[0])
    # saveToDB = DealToDB()
    # saveToDB.toDB()
    # testreturn=saveToDB.passValue('all')
    # print(testreturn)




