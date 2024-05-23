from django.shortcuts import render
from .context_processors import user_info
from user.models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about_us.html')


def services(request):
    return render(request, 'services.html')

def blog(request):
    blogs = Blog.objects.all()
    images = [i for i in blogs]

    return render(request, 'blog.html', {'blogs':blogs})

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact_us.html')

