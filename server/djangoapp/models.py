from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# CarMake model to store information about a car's make
class CarMake(models.Model):
    # The name of the car make (e.g., Ford, Honda)
    name = models.CharField(max_length=100)
    # A brief description of the car make
    description = models.TextField()

    # The __str__ method provides a human-readable 
    # representation of the object.
    # It will be used in the Django admin site and elsewhere.
    def __str__(self):
        return self.name


# CarModel model to store information about a specific car model
class CarModel(models.Model):
    # Many-to-one relationship to the CarMake model.
    # A single CarMake can have multiple CarModels.
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID, which will be used to link this model to a dealership
    # in the Cloudant database.
    dealer_id = models.IntegerField()

    # The name of the car model (e.g., Mustang, Civic)
    name = models.CharField(max_length=100)

    # A list of tuples for the car type choices.
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan')
    ]
    # The car's type, using the choices defined above.
    type = models.CharField(max_length=15, choices=CAR_TYPES)

    # The year the car was made, with validation to ensure the value
    # is within the specified range.
    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

    # The __str__ method returns a combination of the car make and model name
    # for a more descriptive representation.
    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
