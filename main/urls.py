from django.urls import path, include
from .views import *

urlpatterns = [
    # home
    path('', home, name='home')

]