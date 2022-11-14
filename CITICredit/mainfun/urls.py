from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('creditcarddetails', views.creditcarddetails, name='creditcarddetails'),
    path('empdetails', views.empdetails, name='empdetails'),
    path('custdetails', views.custdetails, name='custdetails'),
    path('departments', views.departments, name='departments'),
]
