from django.contrib import admin

from api_server.models import *

# Register your models here.

admin.site.register([Account, Parent, Teacher, SysAdmin])
