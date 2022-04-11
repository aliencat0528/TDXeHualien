from django.contrib import admin

# import sys
# sys.path.append("C:\\herokuenv\\eHualien")
# for sp in sys.path:
#     print(sp)

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eHualien.settings')
#
import django
django.setup()
#
# print("adminPATH",os.getcwd())
# os.chdir('C:\\herokuenv\\eHualien')
# print("changeAdminPATH",os.getcwd())



#import models
from tdxDemo.models import parkInfoDB

#from tdxDemo.models import parkInfoDB

# Register your models here.
# admin.site.register(parkInfoDB)
# print(admin.site)
# print(parkInfoDB.objects.all())