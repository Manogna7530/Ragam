from django.urls import path
from Ganamapp.views import *

urlpatterns = [
    path('demo',demo, name = "demo"),
]