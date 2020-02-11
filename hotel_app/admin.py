from django.contrib import admin
from hotel_app.models import Bed_type, Booking, Client, Room_type
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'room_number', 'room_type', 'mobile')
    model = Client

# admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Room_type)
admin.site.register(Bed_type)
