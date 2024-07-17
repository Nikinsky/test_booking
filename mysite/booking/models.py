from django.db import models


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=32)
    description = models.TextField()
    address = models.CharField(max_length=32)
    city = models.CharField(max_length=32, verbose_name='Sity')
    country = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name_hotel} - {self.country}'


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.SmallIntegerField(default=0)
    capacity = models.PositiveSmallIntegerField(default=0)
    price_per_night = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.hotel} - kvartira {self.room_number}'


class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='room_images/')


class Booking(models.Model):
    user = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = (
        ('bron', 'bron'),
        ('svobodyi', 'svobodnyi'),
        ('zanyt', 'zanyt'),
    )

    status = models.CharField(max_length=16, choices=STATUS_CHOICES)