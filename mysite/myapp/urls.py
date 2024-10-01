from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    path('lic/', views.lic, name='lic'),
    path('activate_lic/', views.activate_lic, name='activate_lic'),
    path('key_activate/', views.key_activate, name='key_activate'),

    path('update_operator_profile/', views.update_operator_profile, name='update_operator_profile'),

    path('operatorlist/', views.operatorlist, name='operatorlist'),
    path('operatorupdate/<int:id>/', views.operatorupdate, name='operatorupdate'),
    path('save_operator/', views.save_operator, name='save_operator'),
    path('', views.linelist, name='linelist'),
    path('updatehr/', views.updatehr, name='updatehr'),
    path('update_line_target/', views.update_line_target, name='update_line_target'),
    path('update_color_percent/', views.update_color_percent, name='update_color_percent'),
    path('operator_delete/<int:id>/', views.operator_delete, name='operator_delete'),
    path('operatortarget/<int:id>/', views.operatortarget, name='operatortarget'),
    path('operatoratt/<int:id>/', views.operatoratt, name='operatoratt'),
    path('operator_point_filter/', views.operator_point_filter, name='operator_point_filter'),
    path('operator_profile_update/', views.operator_profile_update, name='operator_profile_update'),
    path('save_att_daily/', views.save_att_daily, name='save_att_daily'),
    path('daily_rep_view/', views.daily_rep_view, name='daily_rep_view'),
    path('save_daily_rep_view/', views.save_daily_rep_view, name='save_daily_rep_view'),
    path('daily_rep_filter_by_line/<int:id>/', views.daily_rep_filter_by_line, name='daily_rep_filter_by_line'),
    path('daily_rep_filter_operator/<int:id>/', views.daily_rep_filter_operator, name='daily_rep_filter_operator'),
    path('daily_rep_filter_bydate/', views.daily_rep_filter_bydate, name='daily_rep_filter_bydate'),
    path('monthly_report/', views.monthly_report, name='monthly_report'),
    path('dailyrep_delete/<int:id>/', views.dailyrep_delete, name='dailyrep_delete'),
    path('backdate_dataentry/', views.backdate_dataentry, name='backdate_dataentry'),

    path('attendance_backdate/', views.attendance_backdate, name='attendance_backdate'),
    path('save_attendance_backdate/', views.save_attendance_backdate, name='save_attendance_backdate'),

    path('workhour/', views.workhour, name='workhour'),
    path('changehrstatus/', views.changehrstatus,name='changehrstatus'),
    path('optortargetrep/', views.optortargetrep, name='optortargetrep'),
    path('hourlydata/', views.hourlydata, name='hourlydata'),
    path('monthly_filterby_line/', views.monthly_filterby_line, name='monthly_filterby_line'),
    path('reportbyoperator/<int:id>/', views.reportbyoperator, name='reportbyoperator'),
    path('update_combine/<int:id>/', views.update_combine, name='update_combine'),
    path('daily_rep_update/', views.daily_rep_update, name='daily_rep_update'),
    path('daily_line_attendance/', views.daily_line_attendance, name='daily_line_attendance'),

    #search
    path('daily_rep_search/', views.daily_rep_search, name='daily_rep_search'),
    path('delete_datentry/', views.delete_datentry, name='delete_datentry'),
    path('supervisor_point_filter/', views.supervisor_point_filter, name='supervisor_point_filter'),

    #DueDate
    path('duedatefilter/', views.duedatefilter, name='duedatefilter'),
    path('duedatefilter_by_line/', views.duedatefilter_by_line, name='duedatefilter_by_line'),
    path('backdate_data_sync/', views.backdate_data_sync, name='backdate_data_sync'),
    
    #Report
    path('report_groupby_operator/', views.report_groupby_operator, name='report_groupby_operator'),
    path('operator_reportgroup/', views.operator_reportgroup, name='operator_reportgroup'),
    path('operator_reportgroup_filter/<int:id>/', views.operator_reportgroup_filter, name='operator_reportgroup_filter'),
    path('line_operator_dash/', views.line_operator_dash, name='line_operator_dash'),
    path('operator_report_by_date/', views.operator_report_by_date, name='operator_report_by_date'),
    path('supervisor_line_filter/<int:id>/', views.supervisor_line_filter, name='supervisor_line_filter'),
    path('supervisor_result_filter', views.supervisor_result_filter, name='supervisor_result_filter'),
    path('redcolor_by_supervisor/', views.redcolor_by_supervisor, name='redcolor_by_supervisor'),
    path('supervisor_getdaily_filter/', views.supervisor_getdaily_filter, name='supervisor_getdaily_filter'),

    path('one_month_red_color/', views.one_month_red_color, name='one_month_red_color'),
    path('one_month_success_color/', views.one_month_success_color, name='one_month_success_color'),
    path('one_month_filter/', views.one_month_filter, name='one_month_filter'),

    path('one_week_filter/', views.one_week_filter, name='one_week_filter'),
    path('one_week_success/', views.one_week_success, name='one_week_success'),
    path('one_week_danger/', views.one_week_danger, name='one_week_danger'),

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

    path('operator_target_filter/', views.operator_target_filter, name='operator_target_filter'),
    path('operator_target_point_filter/', views.operator_target_point_filter, name='operator_target_point_filter'),

    #Test
    path('monday_week/', views.monday_week, name='monday_week'),
    path('testpref/', views.testpref, name='testpref'),
    path('dailyreport_selectrelated/', views.dailyreport_selectrelated, name='dailyreport_selectrelated'),
    
    path('daily_rep_update_ajax/', views.daily_rep_update_ajax, name='daily_rep_update_ajax'),
    

]