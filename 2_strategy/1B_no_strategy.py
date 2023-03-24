"""
An implementation using inheritance.
"""
from abc import ABC, abstractmethod

class ClothesCleaner(ABC):
    @abstractmethod
    def clean(self):
        pass

class NoSpotCleaner(ClothesCleaner):
    def clean(self):
        print("Wash clothes as usual.")

class CoffeeSpotCleaner(ClothesCleaner):
    def clean(self):
        print("Apply baking soda and a bit of water to the stain. Scrub for some minutes.")
        print("Wash clothes as usual.")

class WineSpotCleaner(ClothesCleaner):
    def clean(self):
        print("Put some salt on the stain. Wait for five minutes.")
        print("Wash clothes as usual.")


# Client code
clothes_cleaner = WineSpotCleaner()
clothes_cleaner.clean()
