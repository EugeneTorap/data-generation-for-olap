import random
import string
from faker import Faker

from api.models import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

RANGE = 100000
T_RANGE = 90000


class RecipeView(viewsets.ViewSet):
    queryset = City.objects.all()

    @action(detail=False)
    def get(self, request, pk=None):
        faker = Faker()

        cities = []
        for i in range(80):
            cities.append(City(name=faker.city(), population=random.randint(30000, 10000000)))
            print(f'{i} -- City')

        City.objects.bulk_create(cities)

        cars = []
        for i in range(RANGE):
            car_number = ''
            for j in range(2):
                car_number += random.choice(string.ascii_uppercase)

            car_number += '-'
            for j in range(4):
                car_number += str(random.randint(0, 9))

            cars.append(Car(number=car_number, carrying_capacity=random.uniform(500, 12000)))
            print(f'{i} -- Car')

        Car.objects.bulk_create(cars)

        drivers = []
        for i in range(RANGE):
            drivers.append(Driver(first_name=faker.first_name(), last_name=faker.last_name(),
                                  age=random.randint(18, 54), car_id=i + 1))
            print(f'{i} -- Driver')

        Driver.objects.bulk_create(drivers)

        clients = []
        for i in range(RANGE):
            clients.append(Client(name=faker.name()))
            print(f'{i} -- Client')

        Client.objects.bulk_create(clients)

        cargo_list = []
        counter = 0
        for i in range(T_RANGE):
            object_id = i + 1

            counter = counter + 1

            if counter % 70 == 0:
                counter = 1

            order_date = faker.date_time_between(start_date="-30y", end_date="now", tzinfo=None)
            letters_and_digits = string.ascii_letters + string.digits
            cargo_name = ''.join(random.choice(letters_and_digits) for i in range(18))

            cargo_list.append(Cargo(name=cargo_name, weight=random.uniform(5, 50), price=random.randint(1, 15),
                                    date=order_date, client_id=object_id, car_id=object_id, start_city_id=counter,
                                    finish_city_id=counter + 5))
            print(f'{i} -- Cargo')

        Cargo.objects.bulk_create(cargo_list)

        return Response(True)
