# Generated by Django 2.2.2 on 2022-04-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tdxDemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='parkInfoDB',
            fields=[
                ('CarParkID', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('CarParkName', models.CharField(max_length=60, unique=True)),
                ('CarParkRegNo', models.CharField(max_length=30)),
                ('OperatorID', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=80)),
                ('CarParkType', models.IntegerField()),
                ('ParkingGuideType', models.TextField()),
                ('ParkingTypes', models.TextField()),
                ('ParkingSiteTypes', models.TextField()),
                ('ChargeTypes', models.TextField()),
                ('Telephone', models.CharField(max_length=20)),
                ('EmergencyPhone', models.CharField(max_length=20)),
                ('PositionLat', models.FloatField()),
                ('PositionLon', models.FloatField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=50)),
                ('WebURL', models.URLField()),
                ('FareDescription', models.TextField()),
                ('SpecialOfferDescription', models.TextField()),
                ('IsFreeParkingOutOfHours', models.IntegerField()),
                ('VehicleRestriction', models.TextField()),
                ('IsPublic', models.IntegerField()),
                ('OperationType', models.IntegerField()),
                ('LiveOccuppancyAvailable', models.IntegerField()),
                ('EVRechargingAvailable', models.IntegerField()),
                ('MonthlyTicketAvailable', models.IntegerField()),
                ('SeasonTicketAvailable', models.IntegerField()),
                ('ReservationAvailable', models.IntegerField()),
                ('WheelchairAccessible', models.IntegerField()),
                ('OvernightPermitted', models.IntegerField()),
                ('TicketMachine', models.IntegerField()),
                ('Toilet', models.IntegerField()),
                ('Restaurant', models.IntegerField()),
                ('GasStation', models.IntegerField()),
                ('Shop', models.IntegerField()),
                ('Gated', models.IntegerField()),
                ('Lighting', models.IntegerField()),
                ('SecureParking', models.IntegerField()),
                ('TicketOffice', models.IntegerField()),
                ('ProhibitedForAnyHazardousMaterialLoads', models.IntegerField()),
                ('SecurityGuard', models.IntegerField()),
                ('Supervision', models.IntegerField()),
                ('LandMark', models.CharField(max_length=50)),
                ('BuildingName', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=13)),
                ('CityCode', models.CharField(max_length=5)),
            ],
        ),
    ]
