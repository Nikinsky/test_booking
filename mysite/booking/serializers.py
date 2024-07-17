from rest_framework import serializers
from .models import Hotel, Room, Booking


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name_hotel', 'description', 'address', 'city', 'country']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'