from django.urls import path, include
from .views import *

urlpatterns = [
    path('register', register_view, name='register_user' ),
    path('login', login_view, name='login_view'),
    path('change-profile', change_profile, name='change_profile'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),



]