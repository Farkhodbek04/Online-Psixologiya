from django.urls import path, include
from .views import *

urlpatterns = [
    # home
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),



]