"""
An implementation without using any Design Patterns.
"""
from abc import abstractmethod, ABC

@abstractmethod
class Cake(ABC):
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


# Client code
fancy_cake = FancyCake(
    base="A simple vanilla base.",
    filling="Marmalade",
    frosting="Buttercream")

fancy_cake.describe()

another_fancy_cake = FancyCake(
    base="A simple vanilla base.",
    filling="Marmalade",
    frosting="Buttercream")

another_fancy_cake.describe()
