from django import forms
from django.forms import ValidationError
from django.core import validators
from django.contrib.auth.models import User
from hotel_app.models import UserInfo, Booking, Client


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

#--------------------------------------------------------------------------------

class FormBooking(forms.ModelForm):

    class Meta():
        model = Booking
        fields = ('client_id','check_in','check_out','bed_type', 'special_req', 'start_date', 'end_date', 'room_number')

class FormClient(forms.ModelForm):

    class Meta():
        model = Client
        fields = ('first_name', 'last_name', 'dob', 'gender', 'email', 'address1', 'address2', 'phone', 'mobile', 'room_type')
