from django.contrib import admin
from django.urls import path
from AppPageCount import views

urlpatterns = [
    path("",views.index, name="index"),
]
