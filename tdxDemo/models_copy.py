from django.db import models
import sys
import os
import django
#
# sys.path.append("C:\\herokuenv\\eHualien")


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eHualien.settings')
django.setup()
#print("modelPATH::",os.getcwd())

#Create your models here.

class parkInfoDB(models.Model):
    #CarParkShortName,Geometry,ParkingAreas,ImageURLs,FareURL,ReservationURL,ReservationDescription,LocationMapURL,TownName,TownID
    CarParkID=models.CharField(max_length=15,null=False,primary_key=True,unique=True)
    CarParkName=models.CharField(max_length=60,null=False,unique=True)
    CarParkRegNo=models.CharField(max_length=30)
    OperatorID=models.CharField(max_length=20)
    Description=models.CharField(max_length=80)
    CarParkType=models.IntegerField()
    ParkingGuideType=models.TextField()
    ParkingTypes=models.TextField()
    ParkingSiteTypes=models.TextField()
    ChargeTypes=models.TextField()
    Telephone=models.CharField(max_length=15)
    EmergencyPhone=models.CharField(max_length=12)
    PositionLat=models.FloatField(null=False)
    PositionLon=models.FloatField(null=False)
    Email=models.EmailField(max_length=254)
    Address=models.CharField(max_length=50,null=False)
    WebURL=models.URLField()
    FareDescription=models.TextField()
    SpecialOfferDescription=models.TextField()
    IsFreeParkingOutOfHours=models.IntegerField()
    VehicleRestriction=models.TextField()
    IsPublic=models.IntegerField()
    OperationType=models.IntegerField()
    LiveOccuppancyAvailable=models.IntegerField()
    EVRechargingAvailable=models.IntegerField()
    MonthlyTicketAvailable=models.IntegerField()
    SeasonTicketAvailable=models.IntegerField()
    ReservationAvailable=models.IntegerField()
    WheelchairAccessible=models.IntegerField()
    OvernightPermitted=models.IntegerField()
    TicketMachine=models.IntegerField()
    Toilet=models.IntegerField()
    Restaurant=models.IntegerField()
    GasStation=models.IntegerField()
    Shop=models.IntegerField()
    Gated=models.IntegerField()
    Lighting=models.IntegerField()
    SecureParking=models.IntegerField()
    TicketOffice=models.IntegerField()
    ProhibitedForAnyHazardousMaterialLoads=models.IntegerField()
    SecurityGuard=models.IntegerField()
    Supervision=models.IntegerField()
    LandMark=models.CharField(max_length=50)
    BuildingName=models.CharField(max_length=50)
    City=models.CharField(max_length=13)
    CityCode=models.CharField(max_length=5)





