from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(line)
admin.site.register(operator)
admin.site.register(daily_report)
admin.site.register(workinghour)
admin.site.register(hourlytargetrep)
admin.site.register(operatortargetrep)
admin.site.register(opreport)