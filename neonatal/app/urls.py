from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login_view',login_view,name='login_view'),
    path('signup',signup,name='signup'),
    path('logout_view',logout_view,name='logout_view'),
    path('food',food,name='food'),
    path('workout',workout,name='workout'),
    path('vaccination',vaccination,name='vaccination'),
    path('Center',Center,name='Center'),
    path('Scheme',Scheme,name='Scheme'),
    path('chatbot',chatbot,name='chatbot'),
    path('Appointment',Appointment,name='Appointment')

]
