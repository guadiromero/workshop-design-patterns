# 4. Template Method

The Template Method belongs to the **behavioral** category. It defines the steps of an algorithm in a base class and allows subclasses to override those steps.

## A simple example

### Before

We want to build an algorithm for making different kinds of mate, e.g., classic mate, mate from Córdoba, and tereré (cold mate). A monolithic algorithm would look like this:

```python
class Mate:
    def make_mate(self, type):
        # Get ingredients
        if type == "classic":
            print("Get yerba and 1/5 liter of water.\n")
        elif type == "cordobés":
            print("Get yerba, 1/5 liter of water and herbs.\n")
        elif type == "tereré":
            print("Get yerba, 3 grapefruits and ice cubes.\n")

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Add herbs
        if type == "cordobés":
            print("Put some herbs inside of the mate cup.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


# Client code
Mate().make_mate("cordobés")
```

The problem with this implementation is that the algorithm uses a lot of conditional statements, making it difficult to read and extend. A cleaner implementation would use a different class for each kind of mate, so that adding a new type wouldn't require to modify any existing code.

```python
class ClassicMate:
    def make_mate(self):
        # Get ingredients
        print("Get yerba and 1/5 liter of water.\n")  # Customized step

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


class MateCordooobes:
    def make_mate(self):
        # Get ingredients
        print("Get yerba, 1/5 liter of water and herbs.\n")  # Customized step

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Add herbs
        print("Put some herbs inside of the mate cup.\n")  # Extra step

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


class Terere:
    def make_mate(self):
        # Get ingredients
        print("Get yerba, 3 grapefruits and ice cubes.\n")  # Customized step

        # Prepare water
        print("Squeeze the grapefruits and add the ice cubes to the juice.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


# Client code
MateCordooobes().make_mate()
```

This version of the code, however, introduces a lot of duplication for steps that are common to different kinds of mate, e.g., fill with yerba, pour water, enjoy. This can be improved if we make use of the Template Method.

### After

We create an abstract class `Mate` and break down the algorithm in individual methods for each of the steps. We then create a Template Method, in this case, `make_mate()`, which calls all of those steps in order.

There are three different types of steps that we can implement:

- **Abstract steps:** They must be overriden by every subclass. In Python, we can enforce this using the `@abstractmethod` decorator. In our sample code, `get_ingredients()` is an abstract method. 
- **Optional steps:** They have a default implementation in the base class and can (but do not have to) be overriden by subclasses. Examples of optional steps are `prepare_water()`, `fill_with_yerba()`, `pour_water()` and `enjoy()`.
- **Hooks:** These are optional steps with an empty body. If it is not overriden, the step does not have any effect, it is "skipped". A hook in our code is, for example, `add_herbs()`.

```python
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
```

Afterwards, we can build subclasses of the `Mate` class, such as `ClassicMate`, `MateCordooobes` and `Terere`. Observe how the abstract method `get_ingredients()` is overriden by every subclass, as it is mandatory to do so. The optional step `prepare_water()` is overriden only by the subclass `Terere`, because the other ones can simply use the default implementation. The `MateCordooobes` subclass implements the hook `add_herbs()`. The other subclasses do not do so, and therefore skip this step.

```python
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
```
