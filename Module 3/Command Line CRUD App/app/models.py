from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    year = models.IntegerField()
    accident_reported = models.BooleanField(default=False)

def create_car(make, model, color, year, accident_reported):
    car = Car.objects.create(make=make, model=model, color=color, year=year, accident_reported=accident_reported)
    return car

def view_all():
    return Car.objects.all()

def find_by_accident_reported():
    car = Car.objects.filter(accident_reported=False)
    if not car:
        return None
    else:
        return car

def find_by_make(make):
    car = Car.objects.get(make=make)
    if not car:
        return None
    else:
        return car

def update(model, accident_update):
    try:
        car = find_by_make(model)
        if car:
            car.accident_reported = accident_update
            car.save()
            return car
    except Exception as error:
        return str(error)
    
def delete_car(model):
    car = Car.objects.get(model=model).delete()
    return car