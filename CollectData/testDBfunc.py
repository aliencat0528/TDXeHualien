
# -------------------save to DB--------------------
# with open('ParkSort.csv', encoding="utf-8") as file:
#     sortData = file.read()
#     sortData = eval(sortData)
#     eachsd=[sd for sd in sortData]
#
#     # for esd in eachsd:
#     #     for idx in list(esd.keys()):
#     #         print(idx, "=", esd.get(idx))
#     for esd in eachsd:
#         pass
#         #sk=list(esd.keys())
#         #db=parkInfoDB.objects.create(sk[0]=esd.get(sk[0]),sk[1]=esd.get(sk[1]),sk[2]=esd.get(sk[2]),sk[3]=esd.get(sk[3]),sk[4]=esd.get(sk[4]),sk[5]=esd.get(sk[5]),sk[6]=esd.get(sk[6]),sk[7]=esd.get(sk[7]),sk[8]=esd.get(sk[8]),sk[9]=esd.get(sk[9]),sk[10]=esd.get(sk[10]),sk[11]=esd.get(sk[11]),sk[12]=esd.get(sk[12]),sk[13]=esd.get(sk[13]),sk[14]=esd.get(sk[14]),sk[15]=esd.get(sk[15]),sk[16]=esd.get(sk[16]),sk[17]=esd.get(sk[17]),sk[18]=esd.get(sk[18]),sk[19]=esd.get(sk[19]),sk[20]=esd.get(sk[20]),sk[21]=esd.get(sk[21]),sk[22]=esd.get(sk[22]),sk[23]=esd.get(sk[23]),sk[24]=esd.get(sk[24]),sk[25]=esd.get(sk[25]),sk[26]=esd.get(sk[26]),sk[27]=esd.get(sk[27]),sk[28]=esd.get(sk[28]),sk[29]=esd.get(sk[29]),sk[30]=esd.get(sk[30]),sk[31]=esd.get(sk[31]),sk[32]=esd.get(sk[32]),sk[33]=esd.get(sk[33]),sk[34]=esd.get(sk[34]),sk[35]=esd.get(sk[35]),sk[36]=esd.get(sk[36]),sk[37]=esd.get(sk[37]),sk[38]=esd.get(sk[38]),sk[39]=esd.get(sk[39]),sk[40]=esd.get(sk[40]),sk[41]=esd.get(sk[41]),sk[42]=esd.get(sk[42]),sk[43]=esd.get(sk[43]),sk[44]=esd.get(sk[44]),sk[45]=esd.get(sk[45]))
#         #db=parkInfoDB.objects.create(CarParkID=esd.get(sk['CarParkID']),CarParkName=esd.get(sk['CarParkName']),CarParkRegNo=esd.get(sk['CarParkRegNo']),OperatorID=esd.get(sk['OperatorID']),Description=esd.get(sk['Description']),CarParkType=esd.get(sk['CarParkType']),ParkingGuideType=esd.get('ParkingGuideType'),ParkingTypes=esd.get('ParkingTypes'),ParkingSiteTypes=esd.get(sk[8]),ChargeTypes=esd.get(sk[9]),Telephone=esd.get('Telephone'),EmergencyPhone=esd.get('EmergencyPhone'),PositionLat=esd.get('PositionLat'),PositionLon=esd.get('PositionLon'),Email=esd.get('Email']),Address=esd.get('Address'),WebURL=esd.get('WebURL'),FareDescription=esd.get('FareDescription'),SpecialOfferDescription=esd.get('SpecialOfferDescription'),IsFreeParkingOutOfHours=esd.get('IsFreeParkingOutOfHours),VehicleRestriction=esd.get('VehicleRestriction'),IsPublic=esd.get('IsPublic'),OperationType=esd.get('OperationType'),LiveOccuppancyAvailable=esd.get('LiveOccuppancyAvailable'),EVRechargingAvailable=esd.get('EVRechargingAvailable'),MonthlyTicketAvailable=esd.get('MonthlyTicketAvailable'),SeasonTicketAvailable=esd.get('SeasonTicketAvailable'),ReservationAvailable=esd.get('ReservationAvailable'),WheelchairAccessible=esd.get('WheelchairAccessible'),OvernightPermitted=esd.get('OvernightPermitted'),TicketMachine=esd.get('TicketMachine'),Toilet=esd.get(sk[31]),Restaurant=esd.get('Restaurant),GasStation=esd.get('GasStation'),Shop=esd.get('Shop'),Gated=esd.get('Gated'),Lighting=esd.get('Lighting'),SecureParking=esd.get('SecureParking'),TicketOffice=esd.get('TicketOffice'),ProhibitedForAnyHazardousMaterialLoads=esd.get('ProhibitedForAnyHazardousMaterialLoads'),SecurityGuard=esd.get('SecurityGuard'),Supervision=esd.get('Supervision'),LandMark=esd.get('LandMark'),BuildingName=esd.get('BuildingName'),City=esd.get('City'),CityCode=esd.get('CityCode'))
#
#         #print((sk[0],"=",esd.get(sk[0]),sk[1],"=",esd.get(sk[1]),sk[2],"=",esd.get(sk[2]),sk[3],"=",esd.get(sk[3]),sk[4],"=",esd.get(sk[4]),sk[5],"=",esd.get(sk[5]),sk[6],"=",esd.get(sk[6]),sk[7],"=",esd.get(sk[7]),sk[8],"=",esd.get(sk[8]),sk[9],"=",esd.get(sk[9]),sk[10],"=",esd.get(sk[10]),sk[11],"=",esd.get(sk[11]),sk[12],"=",esd.get(sk[12]),sk[13],"=",esd.get(sk[13]),sk[14],"=",esd.get(sk[14]),sk[15],"=",esd.get(sk[15]),sk[16],"=",esd.get(sk[16]),sk[17],"=",esd.get(sk[17]),sk[18],"=",esd.get(sk[18]),sk[19],"=",esd.get(sk[19]),sk[20],"=",esd.get(sk[20]),sk[21],"=",esd.get(sk[21]),sk[22],"=",esd.get(sk[22]),sk[23],"=",esd.get(sk[23]),sk[24],"=",esd.get(sk[24]),sk[25],"=",esd.get(sk[25]),sk[26],"=",esd.get(sk[26]),sk[27],"=",esd.get(sk[27]),sk[28],"=",esd.get(sk[28]),sk[29],"=",esd.get(sk[29]),sk[30],"=",esd.get(sk[30]),sk[31],"=",esd.get(sk[31]),sk[32],"=",esd.get(sk[32]),sk[33],"=",esd.get(sk[33]),sk[34],"=",esd.get(sk[34]),sk[35],"=",esd.get(sk[35]),sk[36],"=",esd.get(sk[36]),sk[37],"=",esd.get(sk[37]),sk[38],"=",esd.get(sk[38]),sk[39],"=",esd.get(sk[39]),sk[40],"=",esd.get(sk[40]),sk[41],"=",esd.get(sk[41]),sk[42],"=",esd.get(sk[42]),sk[43],"=",esd.get(sk[43]),sk[44],"=",esd.get(sk[44]),sk[45],"=",esd.get(sk[45])))
#
# -------------------read from DB--------------------
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eHualien.settings")
import django
django.setup()
from tdxDemo.models import parkInfoDB


# ***test how to cnt distance by use db param***

# SELECT CarParkName, PositionLat ,PositionLon , (
#       6371 * acos (
#       cos ( radians(25.030094) )
#       * cos( radians( PositionLat ) )
#       * cos( radians( PositionLon ) - radians(121.557377) )
#       + sin ( radians(25.030094) )
#       * sin( radians( PositionLat ) )
#     )
# ) as Distance
# FROM parkdb.tdxdemo_parkinfodb
# ORDER BY Distance
#




#1
#db.objects.raw('SELECT * FROM table WHERE filed = %s', [param])

# lat=25.030094
# lon=121.557377
#
# rlt = parkInfoDB.objects.raw(
#     'SELECT CarParkID, CarParkName, PositionLat ,PositionLon , \
#     (6371 * acos (cos ( radians(%s) )* cos( radians( PositionLat ) )* cos( radians( PositionLon ) - radians(%s) )+ sin ( radians(%s) )* sin( radians( PositionLat ) ))) AS Distance \
#     FROM tdxdemo_parkinfodb \
#     ORDER BY Distance', [lat,lon,lat])
#
# # print(rlt.values())  #AttributeError: 'RawQuerySet' object has no attribute 'values'
#
# for r in rlt:
#     print(r.CarParkID,r.CarParkName,r.Distance)


#2
# from django.db.models.expressions import RawSQL
# queryset.annotate(val=RawSQL("select col from sometable where othercol = %s", (someparam,)))

from django.db.models.expressions import RawSQL
# testeraw=parkInfoDB.objects.annotate(val=RawSQL('SELECT CarParkID, CarParkName, PositionLat ,PositionLon , \
#      (6371 * acos (cos ( radians(%s) )* cos( radians( PositionLat ) )* cos( radians( PositionLon ) - radians(%s) )+ sin ( radians(%s) )* sin( radians( PositionLat ) ))) AS Distance \
#      FROM tdxdemo_parkinfodb \
#      ORDER BY Distance',(lat,) ))  #django.db.utils.ProgrammingError: not enough arguments for format string

# testeraw=parkInfoDB.objects.annotate(val=RawSQL('SELECT CarParkID, CarParkName FROM tdxdemo_parkinfodb \
#         WHERE distance=%s',())) ?? may fail

# testeraw=parkInfoDB.objects.annotate(val=RawSQL('SELECT CarParkID, CarParkName, PositionLat ,PositionLon , \
#       (6371 * acos (cos ( radians(%s) )* cos( radians( PositionLat ) )* cos( radians( PositionLon ) - radians(%s) )+ sin ( radians(%s) )* sin( radians( PositionLat ) ))) AS Distance \
#       FROM tdxdemo_parkinfodb \
#       ORDER BY Distance',(lat,lon,lat) ))  # django.db.utils.OperationalError: (1241, 'Operand should contain 1 column(s)')


#3
#db.objects.annotate(xxx=mathFunObj(tocntParam))

from django.db.models import *
from django.db.models.functions import *

lat=25.030094
lon=121.557377

funtest = parkInfoDB.objects.annotate(distance=6371 * ACos(
        Cos(Radians(lat))
        * Cos(Radians('PositionLat'))
        * Cos(Radians('PositionLon') - Radians(lon))
        + Sin(Radians(lat))
        * Sin(Radians('PositionLat'))
    , output_field=FloatField())).order_by('distance')
for fv in funtest.values():
    print(fv)

# for fv in parkInfoDB.objects.order_by(funtest).values():
#     print(fv)

# plat=testmp.values()[0].get('PositionLat')
# plon=testmp.values()[0].get('PositionLon')
# funtest=parkInfoDB.objects.annotate(distance=6371*ACos(
#     Cos(Radians(lat))*Cos(Radians(lat))*Cos(Radians(lon) - Radians(lon))+Sin(Radians(lat))*Sin(Radians(lat)),output_field=FloatField()))
# print(funtest.values())

#4
# from django.db.models import F, Func
# queryset.annotate(field_lower=Func(F('field'), function='func')) Func(F('field'), function='func')

# Func(F('field'), function='acos')
# Func(F(Func(F('PositionLat'), function='radians')), function='cos')
# Func(F(Func(F('PositionLat'), function='radians')), function='sin')
# Func(F(Func(F('PositionLon'), function='radians')-Radians(lon)), function='cos')
# 6371*Func(Cos(Radians(lat))*Func(F(Func(F('PositionLat'), function='radians')), function='cos')*Func(F(Func(F('PositionLon'), function='radians')-Radians(lon)), function='cos')+ Sin(Radians(lat))*Func(F(Func(F('PositionLat'), function='radians')), function='sin'), function='acos')
# tstf = parkInfoDB.objects.annotate(distance=6371
#     *Func(Func(Func(lat, function='radians'), function='cos')
#     *Func(Func(F('PositionLat'), function='radians'), function='cos')
#     *Func((Func(F('PositionLon'), function='radians')-Func(Func(lon, function='radians'))), function='cos')
#     +Func(Func(Func(lat, function='radians'), function='sin')
#     *Func(Func(F('PositionLat'), function='radians'), function='sin'), function='acos'),output_field=FloatField())).order_by('distance')
# for fv in tstf.values():
#     print(fv)



# ***history test***
# pdb= parkInfoDB.objects.all()
# pdb.PositionLat = F('PositionLat')
# pdb.PositionLon = F('PositionLon')   #F(PositionLat) <class 'django.db.models.expressions.F'>
# addsum=parkInfoDB.objects.annotate(num_offerings=Count(F('PositionLat') + F('PositionLon')))   #<QuerySet [<parkInfoDB: parkInfoDB object (A00001)>, <parkInfoDB: parkInfoDB object (A00002)>, <parkInfoDB: parkInfoDB object (A00003)>, <parkInfoDB: parkInfoDB object (A00004)>, <parkInfoDB: parkInfoDB object (A00005)>, <parkInfoDB: parkInfoDB object (A00006)>, <parkInfoDB: parkInfoDB object (A00007)>, <parkInfoDB: parkInfoDB object (A00008)>, <parkInfoDB: parkInfoDB object (A00009)>, <parkInfoDB: parkInfoDB object (A00010)>, <parkInfoDB: parkInfoDB object (A00011)>, <parkInfoDB: parkInfoDB object (A00012)>, <parkInfoDB: parkInfoDB object (A00013)>, <parkInfoDB: parkInfoDB object (A00014)>, <parkInfoDB: parkInfoDB object (A00015)>, <parkInfoDB: parkInfoDB object (A00016)>, <parkInfoDB: parkInfoDB object (A00017)>, <parkInfoDB: parkInfoDB object (A00018)>, <parkInfoDB: parkInfoDB object (A00019)>, <parkInfoDB: parkInfoDB object (A00021)>, '...(remaining elements truncated)...']>
# print(parkInfoDB.PositionLat)   #<django.db.models.query_utils.DeferredAttribute object at 0x000002123856CC88>
# print(F('PositionLat'),type(F('PositionLat')))   #F(PositionLat) <class 'django.db.models.expressions.F'>
# print(addsum.get())   #models.MultipleObjectsReturned: get() returned more than one parkInfoDB -- it returned 47!
# for a in addsum:
#     print(a.get())  #AttributeError: 'parkInfoDB' object has no attribute 'get'



