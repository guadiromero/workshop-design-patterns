# 2. Strategy

With the strategy pattern, we can define a family of algorithms, encapsulate each one in a separate class, and make them interchangeable. This pattern belongs to the **behavioral** category.

## A simple example

Imagine that we want to create a product that cleans clothes. First, it needs to remove stains with a specific technique depending on the type of stain (coffee, wine, etc.), and then it can proceed to wash the clothes as usual with water and soap.

### Before

We can think of a straight-forward implementation using conditional statements for each type of stain, as in the example below.

```python
# Application code

class ClothesCleaner:
    def clean(self, stain):
        # Remove stains
        if stain == "coffee":
            print("Apply baking soda and a bit of water to the stain. Scrub for some minutes.")
        elif stain == "wine":
            print("Put some salt on the stain. Wait for five minutes.")

        # Proceed with washing cycle
        print("Wash clothes as usual.")
```

```python
# Client code

clothes_cleaner = ClothesCleaner()
clothes_cleaner.clean("wine")
```

The issue with this implementation is that, as we add support to remove new types of stains, we have to introduce more conditional statements, making the class very difficult to read and maintain. 

We could instead use inheritance, so that we can have an abstract clothes cleaner class and a set of subclasses corresponding to each type of stain.

```python
# Application code

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
```

```python
# Client code

clothes_cleaner = WineSpotCleaner()
clothes_cleaner.clean()
```

However, this alternative implementation poses two other problems. First, it doesn’t allow us to change the type of spot treatment at runtime, as this is decided already when initializing the cleaner. The other problem with this approach is that we produce a lot of code duplication, in this case, for the second step where we wash the clothes. This part could be shared independently of the type of spot treatment in the previous step.

### After

We can solve all of these issues by making use of the Strategy pattern, as in the example below. 

```python
# Application code

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
```

```python
# Client code
spot_treatment_strategy = WineSpotTreatmentStrategy()
clothes_cleaner = ClothesCleaner(spot_treatment_strategy)
clothes_cleaner.clean()
```

We define an abstract class for the spot treatment algorithm (`SpotTreatmentStrategy`) and subclasses that encapsulate each algorithm corresponding to a specific kind of stain (`NoSpotTreatmentStrategy`, `CoffeeSpotTreatmentStrategy`, `WineSpotTreatmentStrategy`). Thanks to this modularization in different classes, we do not need to change existing code if we want to add support for a new type of stain. We only need to add a new class, e.g., `DeodorantSpotTreatmentStrategy`. This respects the **Open/Closed Principle.**

Another benefit of using the Strategy pattern is that it allows us to change the algorithm to use at runtime. We can initialize the `ClothesCleaner` once, and define the type of spot treatment later or change it as many times as we want. We simply pass the appropriate strategy when calling its `clean()` method.
