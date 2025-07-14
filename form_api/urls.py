from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/forms/wheel-specifications', WheelSpecsFormCreateView.as_view(), name='create-wheel-form'),
    path('api/forms/wheel-specifications/list', WheelSpecsFormListView.as_view(), name='list-wheel-forms'),
]