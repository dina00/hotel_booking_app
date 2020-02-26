from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from hotel_app.models import Bed_type, Booking, Client, Room_type
from hotel_app.forms import UserForm, FormBooking, FormClient
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout  # for later
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.forms import formset_factory
from django.forms import modelformset_factory

# Create your views here.


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:  # http request
        user_form = UserForm()
    return render(request, 'register.html', {'user_form': user_form,'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('someone tried to login and failed :(')
            print('username: {} password: {}'.format(username, password))
            return HttpResponse('invalid login details supplied')

    else:
        return render(request, 'login.html', {})


def index(request):
    return render(request, 'index.html')


def bookings_list(request):
    bookings_list = Booking.objects.order_by('check_in')
    bookings = {'bookings': bookings_list}
    return render(request, 'booking_list.html', context=bookings)


def book_update(request, id):
    instance = get_object_or_404(Booking, id=id)
    # context={'booking':instance}
    book_form = FormBooking(instance=instance)
    if request.method == "POST":
        book_form = FormBooking(data=request.POST, instance=instance)
        if book_form.is_valid():
            book = book_form.save()
            book.save()
            messages.add_message(request, messages.SUCCESS,'Booking was updated successfully')
            return redirect('hotel_app:bookings_list')
        else:
            print(book_form.errors)
    else:  # http request
        book_form = FormBooking(instance=instance)
    return render(request, 'book_update.html', {'book_form': book_form, 'booking': instance})


def book_add(request):
#    req_booking = Booking.objects.all()
    # roomno=instance.room_number
    #checkout=instance.check_out

    if request.method == "POST":
        book_form = FormBooking(data=request.POST)
        if book_form.is_valid():
            book_form.save()
            messages.add_message(request, messages.SUCCESS,'Booking was added successfully')
            return redirect('hotel_app:bookings_list')
        else:
            print(book_form.errors)
    else:  # http request
        book_form = FormBooking()
    return render(request, 'book_update.html', {'book_form': book_form,})


def book_delete(request, id):
    instance = get_object_or_404(Booking, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,'Booking was deleted successfully')
    return HttpResponseRedirect(reverse('hotel_app:bookings_list'))


# ================================================================================



def client_update(request, id):
    instance = get_object_or_404(Client, id=id)
    # context={'booking':instance}
    client_form = FormClient(instance=instance)
    # the instance inside the form is to display the data already in the record.
    if request.method == "POST":
        client_form = FormClient(data=request.POST, instance=instance)
        if client_form.is_valid():
            client_form.save()
            messages.add_message(request, messages.SUCCESS,'Client was updated successfully')
            return redirect('hotel_app:clients')
        else:
            print(client_form.errors)
    else:  # http request
        client_form = FormClient(instance=instance)
    return render(request, 'client_update.html', {'client_form': client_form, 'client': instance})


def client_delete(request, id):
    instance = get_object_or_404(Client, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,'Client was deleted successfully')
    return HttpResponseRedirect(reverse('hotel_app:clients'))


def client_add(request):
    ClientFormSet = modelformset_factory(Client,form=FormClient,fields=('__all__'), extra=3)
    form = ClientFormSet(queryset=Client.objects.none())
    if request.method == 'POST':
        form = ClientFormSet(request.POST)
        if form.is_valid():
            form.save()
            form = ClientFormSet(queryset=Client.objects.none())
    # display all clients
    queryset = Client.objects.all().order_by('first_name')
    context = {'clients':queryset,'form': form}
    return render(request, 'clients_list.html', context)

def client_display_info(request, id):
    instance=get_object_or_404(Client, id=id)

    return render(request, 'client_display_info.html', {'instance': instance})
