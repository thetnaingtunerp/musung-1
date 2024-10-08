from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(line)
admin.site.register(dailyhour)
# admin.site.register(daily_report)
admin.site.register(workinghour)
admin.site.register(hourlytargetrep)
admin.site.register(operatortargetrep)
admin.site.register(opreport)
admin.site.register(licencedate)
admin.site.register(point)
# admin.site.register(dailyhour)



class operatorAdmin(admin.ModelAdmin):
  list_display = ("name", "line",)
  
admin.site.register(operator, operatorAdmin)


class dailyreportadmin(admin.ModelAdmin):
  list_display = ('operator_name', 'line', 'created_date')
  list_filter = ('created_date','line')
admin.site.register(daily_report, dailyreportadmin)