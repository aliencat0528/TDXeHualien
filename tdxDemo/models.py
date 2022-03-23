from django.db import models
# import sys
# import os
# import django
#
# sys.path.append("C:\\herokuenv\\eHualien")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eHualien.settings')
# django.setup()

# Create your models here.
class parkData(models.Model):
    pid=models.CharField(max_length=15,null=False,primary_key=True,unique=True)
    name=models.CharField(max_length=60,null=False,unique=True)
    regno=models.CharField(max_length=30)
    operatorID=models.CharField(max_length=20)
    description=models.CharField(max_length=80)
    carparktype=models.IntegerField()
    guidetype=models.TextField()
    parkingtype=models.TextField()
    parksitetype=models.TextField()
    chargetype=models.TextField()
    telephone=models.CharField(max_length=12)
    position=models.TextField(null=False)
    email=models.EmailField()
    address=models.CharField(max_length=50,null=False)
    faredescription=models.TextField()
    isfreeoutofhour=models.IntegerField()
    ispublic=models.IntegerField()
    operationtype=models.IntegerField()
    livespaceavailable=models.IntegerField()
    evrchargeavailable=models.IntegerField()
    monthticketavailable=models.IntegerField()
    seasonticketavailable=models.IntegerField()
    reservationavailable=models.IntegerField()
    wheelchairaccessible=models.IntegerField()
    overnightpermit=models.IntegerField()
    ticketmachine=models.IntegerField()
    toliet=models.IntegerField()
    restaurant=models.IntegerField()
    gasstation=models.IntegerField()
    shop=models.IntegerField()
    gated=models.IntegerField()
    lighting=models.IntegerField()
    secureparking=models.IntegerField()
    ticketoffice=models.IntegerField()
    allowloaddangerobject=models.IntegerField()
    securityguard=models.IntegerField()
    supervision=models.IntegerField()
    city=models.CharField(max_length=13)
    citycode=models.CharField(max_length=5)





