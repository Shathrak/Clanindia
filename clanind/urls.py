# example/urls.py
from django.urls import path

from .views import *


urlpatterns = [
   # path('', g_choice),
    #path('', match),
    path('profile/', profile),
    path('', login )
]