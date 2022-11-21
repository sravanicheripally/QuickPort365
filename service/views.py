from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,DomesticForm,InternationalForm, ParcelForm, ServicesForm
from django.contrib.auth import authenticate, login, logout
from .models import Parcel, Services, Domestic


def base(request):
    return render(request,'base.html')

def home(request):
    dm=DomesticForm
    im=InternationalForm
    return render(request,'home.html',{"form":dm,"form1":im})


def parcel(request):
    if request.method == 'POST':
        print(request.POST)
    par = ParcelForm
    ser = ServicesForm
    return render(request, 'parcel.html', {'par': par, 'ser': ser})


def booking(request):
    return render(request,'booking.html')


def tracking(request):
    return render(request, 'tracking.html')


def profile(request):
    return render(request,'profiles.html')


def order_summary(request):
    summary = request.session
    print(summary)
    return render(request, 'order_summary.html')


def sign(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created Successfully !!')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form':fm})


def logins(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/home/')
    else:
      fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})
  else:
    return HttpResponseRedirect('/additem/')


def profile(request):
  if request.user.is_authenticated:
    return render(request, 'profile.html', {'name': request.user})
  else:
    return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
