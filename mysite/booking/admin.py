from django.contrib import admin
from .models import *


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(ImageRoom)
admin.site.register(HotelImage)
admin.site.register(Booking)