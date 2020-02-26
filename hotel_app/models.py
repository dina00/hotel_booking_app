from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError

class Room_type (models.Model):
    type_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(self.type_name)

class Bed_type(models.Model):
    type_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.type_name

class Client (models.Model):
        first_name = models.CharField(max_length=100, blank=True, null=True)
        last_name = models.CharField(max_length=100, blank=True, null=True)
        dob = models.DateField()
        gender = models.CharField(max_length=8)
        email = models.CharField(max_length=100,unique=True)
        address1 = models.CharField(max_length=250)
        address2 = models.CharField(max_length=250)
        phone = models.CharField(max_length=9, unique=True)
        mobile = models.CharField(max_length=12, unique=True)
        room_type = models.ForeignKey(Room_type, on_delete=models.CASCADE)


        def __str__(self):
            full_name = self.first_name+' '+self.last_name
            return full_name

class Booking (models.Model):
    # id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room_number = models.PositiveIntegerField()
    bed_type = models.ForeignKey(Bed_type, on_delete=models.CASCADE)
    special_req = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.client_id.first_name

    def save(self):
        req_booking = Booking.objects.all()
        for x in req_booking:
            if self.room_number == x.room_number and self.check_in <= x.check_out and self.check_in >= x.check_in:
                raise ValidationError('Room not available for this time period.')
            else:
                return super(Booking, self).save()

#-------------------------------------------------------------------------------------

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
