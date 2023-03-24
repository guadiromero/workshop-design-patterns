"""
An implementation using the Factory Method pattern.
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
    @staticmethod
    def bake_cake(cake_type):
        if cake_type == "simple":
            cake = SimpleCake(
                base="A simple vanilla cake.")
        elif cake_type == "fancy":
            cake = FancyCake(
                base="Vanilla cake.",
                filling="Marmalade",
                frosting="Buttercream")
        return cake


# Client code
bakery = CakeFactory

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()

another_fancy_cake = bakery.bake_cake("fancy")
another_fancy_cake.describe()
