from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('operatorlist/', views.operatorlist, name='operatorlist'),
    path('save_operator/', views.save_operator, name='save_operator'),
    path('linelist/', views.linelist, name='linelist'),
    path('update_line_target/', views.update_line_target, name='update_line_target'),
    path('operatortarget/<int:id>/', views.operatortarget, name='operatortarget'),
    path('operatoratt/<int:id>/', views.operatoratt, name='operatoratt'),
    path('save_att_daily/', views.save_att_daily, name='save_att_daily'),
    path('daily_rep_view/', views.daily_rep_view, name='daily_rep_view'),
    path('save_daily_rep_view/', views.save_daily_rep_view, name='save_daily_rep_view'),
    path('daily_rep_filter_by_line/<int:id>/', views.daily_rep_filter_by_line, name='daily_rep_filter_by_line'),
    path('daily_rep_filter_operator/<int:id>/', views.daily_rep_filter_operator, name='daily_rep_filter_operator'),
    path('daily_rep_filter_bydate/', views.daily_rep_filter_bydate, name='daily_rep_filter_bydate'),
    path('monthly_report/', views.monthly_report, name='monthly_report'),

    path('testfor/', views.testfor, name='testfor'),
]