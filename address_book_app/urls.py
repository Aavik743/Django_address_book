from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AddressBookAPI.as_view()),
    path('<str:id_num>/', views.AddressBookAPI.as_view())
]