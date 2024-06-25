from django.urls import path
from django.contrib import admin
from .import views


urlpatterns = [
    path('mahesh_form/', views.Form_Input, name='Form-Input'),
    path('mahesh_display/', views.get_data, name='get_data')
]
