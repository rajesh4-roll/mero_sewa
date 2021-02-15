from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="conatct"),
    path("services",views.services, name="services"),
]
