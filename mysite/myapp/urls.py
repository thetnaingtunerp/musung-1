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

    path('workhour/', views.workhour, name='workhour'),
    path('changehrstatus/', views.changehrstatus,name='changehrstatus'),
    path('optortargetrep/', views.optortargetrep, name='optortargetrep'),
    path('hourlydata/', views.hourlydata, name='hourlydata'),
    path('rank_by_line/', views.rank_by_line, name='rank_by_line'),

    #update hour
    path('update_h1/', views.update_h1, name='update_h1'),
    path('update_h2/', views.update_h2, name='update_h2'),
    path('update_h3/', views.update_h3, name='update_h3'),
    path('update_h4/', views.update_h4, name='update_h4'),
    path('update_h5/', views.update_h5, name='update_h5'),
    path('update_h6/', views.update_h6, name='update_h6'),
    path('update_h7/', views.update_h7, name='update_h7'),
    path('update_h8/', views.update_h8, name='update_h8'),
    path('update_h9/', views.update_h9, name='update_h9'),
    path('update_h10/', views.update_h10, name='update_h10'),
    path('update_h11/', views.update_h11, name='update_h11'),
    path('update_h12/', views.update_h12, name='update_h12'),


]