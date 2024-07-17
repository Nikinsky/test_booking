# Generated by Django 5.0.7 on 2024-07-16 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hotel', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32, verbose_name='Sity')),
                ('country', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_image', models.ImageField(upload_to='hotel_image/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.SmallIntegerField(default=0)),
                ('capacity', models.PositiveSmallIntegerField(default=0)),
                ('price_per_night', models.PositiveIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='room_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('check_in_date', models.DateTimeField()),
                ('check_out_date', models.DateTimeField()),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('bron', 'bron'), ('svobodyi', 'svobodnyi'), ('zanyt', 'zanyt')], max_length=16)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
            ],
        ),
    ]
