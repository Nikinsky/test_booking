from .models import Hotel, Room, Booking
from .serializers import HotelSerializers, RoomSerializers, BookingSerializers
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import RoomFilter
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['city', 'country']
    search_fields = ['name_hotel']
    permission_classes = [permissions.AllowAny]
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers