from django.urls import path
from .views import *

urlpatterns = [
    path('', MainpageView.as_view(), name = 'mainpage'),
]