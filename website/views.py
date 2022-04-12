from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')


def login(request):
    if request.method=="POST":

        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('/login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # number = request.POST.get('number')
        email = request.POST.get("email")
        # address = request.POST.get("address")
        # pincode = request.POST.get("pincode")
        password = request.POST.get("password")
        Cpassword = request.POST.get("password1")

        if password==Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matching...")
            return redirect('/register')
        return redirect('/')
    else:
        return render(request,'register.html')

        return HttpResponse(" Welcome ")











