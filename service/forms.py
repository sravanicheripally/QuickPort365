from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Domestic, International, Parcel, Services



class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}


class DomesticForm(forms.ModelForm):
 class Meta:
  model=Domestic
  fields="__all__"


class InternationalForm(forms.ModelForm):
 class Meta:
  model = International
  fields = "__all__"

class ParcelForm(forms.ModelForm):
 class Meta:
  model = Parcel
  fields = "__all__"

class ServicesForm(forms.ModelForm):
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Services
        fields = "__all__"

