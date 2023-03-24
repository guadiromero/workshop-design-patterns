"""
An implementation using the Factory Method pattern, but this time with variants for each object type.
"""
from abc import abstractmethod, ABC

class Cake(ABC):
    @abstractmethod
    def describe(self):
        pass

class SimpleCake(Cake):
    def __init__(self, base):
        self.base = base

    def describe(self):
        print(self.base)

class FancyCake(Cake):
    def __init__(self, base, filling, frosting):
        self.base = base
        self.filling = filling
        self.frosting = frosting

    def describe(self):
        print(self.base)
        print(self.filling)
        print(self.frosting)

class CakeFactory:
    def __init__(self, flavour):
        self.flavour = flavour

    def bake_cake(self, cake_type):
        if cake_type == "simple":
            if self.flavour == "vanilla":
                cake = SimpleCake(
                    base="A simple vanilla cake.")
            elif self.flavour == "chocolate":
                cake = SimpleCake(
                    base="A simple chocolate cake.")
        elif cake_type == "fancy":
            if self.flavour == "vanilla":
                cake = FancyCake(
                    base="Vanilla cake.",
                    filling="Marmalade",
                    frosting="Buttercream")
            elif self.flavour == "chocolate":
                cake = FancyCake(
                    base="Chocolate cake.",
                    filling="Chocolate mousse",
                    frosting="Chocolate glaze")
        return cake


# Client code
bakery = CakeFactory("chocolate")

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()
