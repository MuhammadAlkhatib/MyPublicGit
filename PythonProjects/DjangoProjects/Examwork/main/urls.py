from django.urls import path

from . import views

urlpatterns = [
    path("", views.mywebsite, name="mywebsite"),
    path("index", views.index, name="index"),
]