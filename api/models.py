from django.db import models


class City(models.Model):
    name = models.TextField()
    population = models.IntegerField()

    class Meta:
        db_table = 'city'


class Car(models.Model):
    number = models.TextField()
    carrying_capacity = models.FloatField()

    class Meta:
        db_table = 'car'


class Driver(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='drivers')

    class Meta:
        db_table = 'driver'


class Client(models.Model):
    name = models.TextField()

    class Meta:
        db_table = 'client'


class Cargo(models.Model):
    name = models.TextField()
    weight = models.FloatField()
    price = models.IntegerField()
    date = models.DateTimeField()

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='transportation_list')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='transportation_list')
    start_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='transportation_list_start')
    finish_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='transportation_list_finish')

    class Meta:
        db_table = 'cargo'
