"""
An implementation using the Abstract Factory method.
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

class CakeFactory(ABC):
    @abstractmethod
    def bake_cake(self, cake_type):
        pass

class VanillaCakeFactory(CakeFactory):
    def bake_cake(self, cake_type):
        if cake_type == "simple":
            cake = SimpleCake(
                base="A simple vanilla cake.")
        elif cake_type == "fancy":
            cake = FancyCake(
                base="Vanilla cake.",
                filling="Marmalade",
                frosting="Buttercream")
        return cake

class ChocolateCakeFactory(CakeFactory):
    def bake_cake(self, cake_type):
        if cake_type == "simple":
            cake = SimpleCake(
                base="A simple chocolate cake.")
        elif cake_type == "fancy":
            cake = FancyCake(
                base="Chocolate cake.",
                filling="Chocolate mousse.",
                frosting="Chocolate glaze.")
        return cake

class CakeFactoryProducer:
    def get_factory(self, flavour):
        factories = {
            "vanilla": VanillaCakeFactory,
            "chocolate": ChocolateCakeFactory,
        }

        return factories[flavour]()


# Client code
bakery = CakeFactoryProducer().get_factory("chocolate")

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()
