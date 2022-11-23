import razorpay
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm,DomesticForm,InternationalForm, ParcelForm, ServicesForm
from django.contrib.auth import authenticate, login, logout
from .models import Parcel, Services, Domestic, Details
from django.views.decorators.csrf import csrf_exempt


def base(request):
    return render(request, 'base.html')


def home(request):
    if request.method == 'POST':
        request.session['range'] = request.POST
        print(request.session['range'])
        print('post method')
        return HttpResponseRedirect('parcel')
    range = request.GET.get('range')

    if range == 'Domestic':
        form = DomesticForm

    else:
        form = InternationalForm

    return render(request, 'home.html', {"form": form, 'range': range})


def parcel(request):
    if request.method == 'POST':
        print(request.POST, '......yes')
        request.session['summary'] = request.POST
        print(request.session['summary'])
        return HttpResponseRedirect('summary')
    par = ParcelForm
    ser = ServicesForm
    return render(request, 'parcel.html', {'par': par, 'ser': ser})


def booking(request):
    return render(request, 'booking.html')


def tracking(request):
    return render(request, 'tracking.html')


def profile(request):
    return render(request,'profiles.html')


def order_summary(request):
    summary = request.session['summary']
    print(summary)
    return render(request, 'order_summary.html', {'summary': summary})


def payment_details(request):
        print(request.GET)
        request.session['service'] = request.GET['service']
        print(request.session['service'])
        if request.GET.get('service') == 'Standard':
            price = int(request.session['summary']['item_weight'])*120
            request.session['price'] = price
            days = 3
            return render(request, 'payment_details.html', {'price': price, 'days': days})
        if request.GET.get('service') == 'Premium':
            price = int(request.session['summary']['item_weight']) * 250
            request.session['price'] = price
            days = 1
            return render(request, 'payment_details.html', {'price': price, 'days': days})
        return render(request, 'payment_details.html')


def address_enter(request):
    if request.method == 'POST':
        request.session['address'] = request.POST
        print(request.session['address'])
        return HttpResponseRedirect('payment_options')
    return render(request, 'address.html')


def payment_options(request):
    if request.method == 'POST':
        amount  = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_6lrPUDLV0dRFf9', 'OjNBfOuoD0M8yl3Gkeo9YuJK'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        return render(request, 'payment_options.html', {'price': price, 'delivery': delivery_address})
    price = request.session['price']
    delivery_address = ' '
    delivery_address += request.session['address']['delivery_area']+' ,'
    delivery_address += request.session['address']['delivery_location']+', '
    delivery_address += request.session['address']['delivery_pincode']
    return render(request, 'payment_options.html', {'price': price, 'delivery': delivery_address})


@csrf_exempt
def success(request):

    l = [request.session['summary'],
    request.session['address'],
    request.session['range'],
    request.session['price'],
    request.session['service']]
    order = Details(origin=request.session['range']['origin'], destination=request.session['range']['destination'],
                    item_weight=request.session['summary']['item_weight'],item_name=request.session['summary']['item_name'],
                    date=request.session['summary']['date'], from_whom=request.session['summary']['select'],
                    image=request.session['summary']['image'], services=request.session['service'],
                    price=request.session['price'] )
    order.save()

    if request.GET.get('service') == 'Standard':
        print('Standard')

    else:
        print('Premium')



    return render(request, 'success.html', {'order': order})


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
