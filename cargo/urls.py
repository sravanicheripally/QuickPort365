"""cargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('hom', views.home, name='home'),
    path('book/', views.booking,name='book'),
    path('trac/',views.tracking,name='trac'),
    path('profile/', views.tracking, name='profile'),
    path('sign', views.sign, name='signup'),
    path('login/', views.logins, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('parcel', views.parcel, name='parcel'),
    path('summary', views.order_summary, name='summary'),
    path('payment', views.payment_details, name='payment'),
    path('address', views.address_enter, name='address'),
    path('payment_options', views.payment_options, name='payment_options'),
    path('success', views.success, name='success')
]
