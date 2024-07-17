from django.urls import path
from .views import HotelViewSet, RoomViewSet, BookingViewSet

urlpatterns = [
    path('', HotelViewSet.as_view({'get':'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>', HotelViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}), name='hotel_detail'),

    path('room/', RoomViewSet.as_view({'get':'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}), name='room_detail'),

    path('booking/', BookingViewSet.as_view({'get':'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}), name='booking_detail'),

]
