from django.test import TestCase
from app import models

# Create your tests here.
class TestCar(TestCase):
    def test_can_create_car(self):
        car = models.create_car(
            "Toyota",
            "Tacoma",
            "Blue",
            2008,
            False
        )

        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Tacoma")
        self.assertEqual(car.color, "Blue")
        self.assertEqual(car.year, 2008)
        self.assertFalse(car.accident_reported, False)

    def test_can_view_all_cars(self):
        cars = [
            {
                "make": "Jeep",
                "model": "Wrangler",
                "color": "Black",
                "year": 2012,
                "accident_reported": True,
            },
            {
                "make": "Ford",
                "model": "Ranger",
                "color": "Green",
                "year": 2007,
                "accident_reported": False,
            },
            {
                "make": "Toyota",
                "model": "Tundra",
                "color": "White",
                "year": 2015,
                "accident_reported": True,
            },
        ]

        for car in cars:
            models.create_car(
                car["make"],
                car["model"],
                car["color"],
                car["year"],
                car["accident_reported"],
            )

        view_cars = models.view_all()

        self.assertEqual(len(view_cars), len(cars))

        cars = sorted(cars, key=lambda c: c["make"])
        view_cars = sorted(view_cars, key=lambda c: c.make)

        for data, car in zip(cars, view_cars):
            self.assertEqual(data["make"], car.make)
            self.assertEqual(data["model"], car.model)
            self.assertEqual(data["color"], car.color)
            self.assertEqual(data["year"], car.year)
            self.assertEqual(data["accident_reported"], car.accident_reported)


    def test_can_search_by_accident_reported(self):
        cars = [
            {
                "make": "Toyota",
                "model": "Corolla",
                "color": "Blue",
                "year": 2019,
                "accident_reported": True,
            },
            {
                "make": "Nissan",
                "model": "Altima",
                "color": "Red",
                "year": 2021,
                "accident_reported": False,
            },
            {
                "make": "Jeep",
                "model": "Wrangler",
                "color": "Blue",
                "year": 2010,
                "accident_reported": True,
            },
            {
                "make": "Chrysler",
                "model": "200",
                "color": "Silver",
                "year": 2013,
                "accident_reported": True,
            },
            {
                "make": "Jeep",
                "model": "Grand Cherokee",
                "color": "White",
                "year": 2015,
                "accident_reported": False,
            },
        ]

        for car in cars:
            models.create_car(
                car["make"],
                    car["model"],
                    car["color"],
                    car["year"],
                    car["accident_reported"],
            )

        self.assertEqual(len(models.find_by_accident_reported()), 2)


    def test_can_search_by_make(self):
            cars = [
                {
                    "make": "Toyota",
                    "model": "Tacoma",
                    "color": "Silver",
                    "year": 2005,
                    "accident_reported": True,
                },
                {
                    "make": "Jeep",
                    "model": "Gladiator",
                    "color": "Red",
                    "year": 2018,
                    "accident_reported": False,
                },
                {
                    "make": "Ford",
                    "model": "Mustang",
                    "color": "White",
                    "year": 2019,
                    "accident_reported": False,
                },
            ]

            for car in cars:
                models.create_car(
                    car["make"],
                    car["model"],
                    car["color"],
                    car["year"],
                    car["accident_reported"],
                )

            car = models.find_by_make("Jeep")

            self.assertIsNotNone(car)
            self.assertEqual(car.model, "Gladiator")

    def test_can_update_accident_reported(self):
        cars = [
            {
                "make": "Jeep",
                "model": "Wrangler",
                "color": "Black",
                "year": 2012,
                "accident_reported": True,
            },
            {
                "make": "Ford",
                "model": "Ranger",
                "color": "Green",
                "year": 2007,
                "accident_reported": False,
            },
            {
                "make": "Toyota",
                "model": "Tundra",
                "color": "White",
                "year": 2015,
                "accident_reported": True,
            },
        ]

        for car in cars:
            models.create_car(
                    car["make"],
                    car["model"],
                    car["color"],
                    car["year"],
                    car["accident_reported"],
            )

        models.update("Ford", True)

        self.assertEqual(
            models.find_by_make("Ford").accident_reported, True
        )
    
    def test_can_delete_car(self):
        cars = [
            {
                "make": "Toyota",
                "model": "Corolla",
                "color": "Blue",
                "year": 2019,
                "accident_reported": True,
            },
            {
                "make": "Nissan",
                "model": "Altima",
                "color": "Red",
                "year": 2021,
                "accident_reported": False,
            },
            {
                "make": "Jeep",
                "model": "Wrangler",
                "color": "Blue",
                "year": 2010,
                "accident_reported": True,
            },
            {
                "make": "Chrysler",
                "model": "200",
                "color": "Silver",
                "year": 2013,
                "accident_reported": True,
            },
            {
                "make": "Jeep",
                "model": "Grand Cherokee",
                "color": "White",
                "year": 2015,
                "accident_reported": False,
            },
        ]

        for car in cars:
            models.create_car(
                    car["make"],
                    car["model"],
                    car["color"],
                    car["year"],
                    car["accident_reported"],
            )

        models.delete_car("Corolla")
        self.assertEqual(len(models.view_all()), 4)
        