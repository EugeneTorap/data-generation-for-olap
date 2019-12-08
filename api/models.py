from django.db import models


class Stop(models.Model):
    country = models.TextField()
    city = models.TextField()

    class Meta:
        db_table = 'stop'


class Transport(models.Model):
    fuel = models.FloatField()
    year = models.IntegerField()
    transport_type = models.TextField()

    class Meta:
        db_table = 'transport'


class Ticket(models.Model):
    date = models.DateTimeField()
    seat = models.IntegerField()
    cost = models.FloatField()

    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='tickets')
    start_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='start_tickets')
    finish_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='finish_tickets')

    class Meta:
        db_table = 'ticket'
