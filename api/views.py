import random
import string
from faker import Faker

from api.models import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

RANGE = 100000
T_RANGE = 90000

TRANSPORT_NAMES = [
    'bus', 'taxi', 'train', 'subway', 'ship', 'airplane'
]


class RecipeView(viewsets.ViewSet):
    queryset = Stop.objects.all()

    @action(detail=False)
    def get(self, request, pk=None):
        faker = Faker()

        stops = []
        for i in range(80):
            stops.append(Stop(country=faker.country(), city=faker.city()))
            print(f'{i} -- Stop')

        Stop.objects.bulk_create(stops)

        transports = []
        for i in range(RANGE):
            transports.append(Transport(transport_type=random.choice(TRANSPORT_NAMES), fuel=random.uniform(500, 5500),
                                        year=random.randint(1990, 2019)))
            print(f'{i} -- Transport')

        Transport.objects.bulk_create(transports)

        tickets = []
        counter = 0
        for i in range(T_RANGE):
            counter = counter + 1

            if counter % 70 == 0:
                counter = 1

            order_date = faker.date_time_between(start_date="-10y", end_date="now", tzinfo=None)

            tickets.append(Ticket(seat=random.randint(1, 100), cost=random.uniform(1, 200), date=order_date,
                                  start_stop_id=counter, finish_stop_id=counter + 5, transport_id=counter))
            print(f'{i} -- Ticket')

        Ticket.objects.bulk_create(tickets)

        return Response(True)
