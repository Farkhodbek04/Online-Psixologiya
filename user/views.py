from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def register_view(request):

    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            status = request.POST.get('status')
        except TypeError:
            return HttpResponse("Type error")

        if CustomUser.objects.filter(username=email).exists():
            return HttpResponse('Mavjud email, boshqa kiriting!', status=400)

        user = CustomUser.objects.create_user(username=email, password=password, f_name=f_name, l_name=l_name, status=status)
        user.save()
        login(request, user)
        return HttpResponse('Muvaffaqiyatli royxatdan otdingiz!', status=200)
    return render(request, 'user/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            return HttpResponse('Please provide both username and password', status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Welcome!', status=400) 
        else:
            return HttpResponse('Invalid credentials', status=401)

    return render(request, 'user/login.html')
