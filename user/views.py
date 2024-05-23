from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def register_view(request):

    if request.method == 'POST':
        try:
            email = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            status = request.POST.get('status')
        except TypeError:
            return HttpResponse("Type error")

        if CustomUser.objects.filter(username=email).exists():
            return HttpResponse('Mavjud email, boshqa kiriting!', status=400)

        user = CustomUser.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name, status=status)
        user.save()
        login(request, user)
        return redirect('login_view')
    return render(request, 'user/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return HttpResponse('Please provide both username and password', status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return HttpResponse('Invalid credentials', status=401)

    return render(request, 'user/login.html')

def logout_view(request):
    """
    Logs out the user and redirects them to the home page.
    """
    logout(request)
    return redirect('home')


def change_profile(request):
    return render(request, 'user/change_profile.html')


def profile(request):
    context = {'user': request.user}
    return render(request, 'user/profile.html', context)


