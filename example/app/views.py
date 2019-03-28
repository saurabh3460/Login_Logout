from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, login as user_login, logout, authenticate
from django.urls import reverse

User = get_user_model()


def home(request):
    return HttpResponseRedirect(reverse('signup'))

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'signup.html')

        if request.method == "POST":
            context = {
                "username": request.POST["name"],
                "email": request.POST["email"],
                "password": request.POST["password1"],
            }
            if context["password"] == request.POST["password2"]:
                try:
                    user = User.objects.create_user(**context)
                    user.is_active = True
                    user_login(request, user)
                    return JsonResponse({"status": 200})
                except IntegrityError:
                    return JsonResponse({"status": 400, "msg": "username or email already exits"})

            else: return JsonResponse({"status": "Please enter Valid Password"})
    else: return HttpResponseRedirect(reverse('profile'))



def profile(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            context = {"user": request.user}
            return render(request, 'profile.html', context=context)


def login(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "login.html")

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                user_login(request, user)
                return JsonResponse({"status": 200})
            else:
                return JsonResponse({"status": 400})
    else:
        return HttpResponseRedirect(reverse('profile'))

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))