from django.urls import path, include
from .views import *

urlpatterns = [path('register', register_view, name='register_user' ),
               path('login', login_view, name='login'),
               ]