from django_filters.rest_framework import FilterSet
from .models import Room

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_number': ['exact'],
            'capacity': ['exact'],
            'price_per_night': ['gt','lt']
        }