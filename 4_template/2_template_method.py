"""
An implementation using the Template Method pattern.
"""
from abc import ABC, abstractmethod

class Mate(ABC):
    def make_mate(self):
        self.get_ingredients()
        self.prepare_water()
        self.fill_with_yerba()
        self.add_herbs()
        self.pour_water()
        self.enjoy()

    @abstractmethod
    def get_ingredients(self):
        pass

    def prepare_water(self):
        print("Heat water to 80 degrees Celsius.\n")

    def fill_with_yerba(self):
        print("Fill 3/4 of the mate cup with yerba.\n")

    def add_herbs(self):
        pass

    def pour_water(self):
        print("Pour a bit of water and drink.\n")

    def enjoy(self):
        print("Ay, qué rico está este mate\n"
              "¡Pero qué rico este mate!\n"
              "Y la temperatura justa\n"
              "y el sabor yerbateril\n"
              "acariciando mis papilas.")


class ClassicMate(Mate):
    def get_ingredients(self):
        print("Get yerba and 1/5 liter of water.\n")


class MateCordooobes(Mate):
    def get_ingredients(self):
        print("Get yerba, 1/5 liter of water and herbs.\n")

    def add_herbs(self):
        print("Put some herbs inside of the mate cup.\n")


class Terere(Mate):
    def get_ingredients(self):
        print("Get yerba, 3 grapefruits and ice cubes.\n")

    def prepare_water(self):
        print("Squeeze the grapefruits and add the ice cubes to the juice.\n")


# Client code
MateCordooobes().make_mate()
