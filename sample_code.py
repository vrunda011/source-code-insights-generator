"""Sample code for testing."""

import os
import sys


class Car:
    """This is a Car."""

    def __init__(self, make, model, year):
        """Starts a car."""
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        """Drives the car."""
        self.mileage += miles
        print(f"You drove {miles} miles.")


def greet(name):
    """Says hello."""
    print(f"Hello, {name}!")


def calculate_square(num):
    """Calculates square."""
    return num**2


# Example usage
car1 = Car("Toyota", "Camry", 2022)
print(f"Car: {car1.make} {car1.model} {car1.year}")
car1.drive(100)
print(f"Mileage: {car1.mileage}")

greet("Alice")

result = calculate_square(5)
print(f"Square of 5: {result}")
