"""
An implementation using the Strategy pattern.
"""
from abc import ABC

class SpotTreatmentStrategy(ABC):
    def clean(self):
        pass

class NoSpotTreatmentStrategy(SpotTreatmentStrategy):
    def clean(self):
        pass

class CoffeeSpotTreatmentStrategy(SpotTreatmentStrategy):
    def clean(self):
        print("Apply baking soda and a bit of water to the stain. Scrub for some minutes.")

class WineSpotTreatmentStrategy(SpotTreatmentStrategy):
    def clean(self):
        print("Put some salt on the stain. Wait for five minutes.")

class ClothesCleaner:
    def __init__(self, spot_treatment_strategy=NoSpotTreatmentStrategy()):
        self.spot_treatment_strategy = spot_treatment_strategy

    def set_spot_treatment_strategy(self, spot_treatment_strategy):
        self.spot_treatment_strategy = spot_treatment_strategy

    def clean(self):
        # Remove stains
        self.spot_treatment_strategy.clean()

        # Proceed with washing cycle
        print("Wash clothes as usual.")


# Client code
spot_treatment_strategy = WineSpotTreatmentStrategy()
clothes_cleaner = ClothesCleaner(spot_treatment_strategy)
clothes_cleaner.clean()
