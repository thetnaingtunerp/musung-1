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
]