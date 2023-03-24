# 1. Factory Method & Abstract Factory

Factory Method and Abstract Factory are two related design patterns under the **creational** category. They provide an interface for creating objects in a superclass, without having to specify the exact class of the object that will be created or how it is created.

## Factory Method

### Before

We are building an application that allows our customers to bake two types of cake: a simple cake for lazy afternoons, and a fancy cake for birthdays and special occasions. One consists simply of the base, while the other one has additional filling and frosting, so we need specific classes for each type, with different attributes and method implementations.

```python
# Application code

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
```

The problem with this implementation is that, whenever the client wants to bake a cake, they need to know which class to use for it (e.g., `FancyCake` if they want to bake a birthday cake). They also need to take care of all the creation logic from their side (e.g., specifying which kind of base, filling, frosting).

```python
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
```

### After

With the help of the Factory Method, we can encapsulate the knowledge of which `Cake` subclass to use (`SimpleCake` or `FancyCake`), so the client does not need to take care of that. Note also how the use of the Factory Method aligns with two of the SOLID principles:

- **Single Responsibility Principle:** The product creation code is encapsulated into one specific class that only deals with this logic. If we need to make changes to that logic, we only need to change the `CakeFactory` class.

- **Open/Closed Principle:** We can introduce new types of cake into the application without breaking existing client code. We do it by adding a new concrete class for a cake (e.g., `SuperFancyCake`) and handling its creation inside of `CakeFactory`.

```python
# Application code

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
```

```python
# Client code

bakery = CakeFactory

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()

another_fancy_cake = bakery.bake_cake("fancy")
another_fancy_cake.describe()
```

## Abstract Factory

### Before

We now get new requirements to support different flavours of cake, so that we can bake not only simple and fancy cakes, but also vanilla and chocolate variants of both. We could extend the `CakeFactory` code with conditional statements like in the example below. However, this is not optimal, as our code would become overcrowded with conditional statements as we add new flavours, making it hard to understand and more prone to bugs.

```python
# Application code

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
```

```python
# Client code

bakery = CakeFactory("chocolate")

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()
```

### After

We could solve this issue by making use of the `Abstract Factory` pattern. In addition to the benefits of the `Factory Method`, this pattern provides yet another level of abstraction that allows us to create families of related objects, in this case, cakes with a certain flavour. To add support for a new flavour of cakes, we need to create a new cake factory class, e.g., `CarrotCakeFactory`, and add the mapping to `CakeFactoryProducer`, e.g., "carrot": `CarrotCakeFactory`. As you can see, this helps us respect the **Single Responsibility** and **Open/Closed** Principles.

```python
# Application code

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
```

The client can pass a parameter when instantiating the cake factory, indicating which kind of flavour they want, and the `CakeFactoryProducer` class will take care of the logic behind it.

```python
# Client code

bakery = CakeFactoryProducer().get_factory("chocolate")

fancy_cake = bakery.bake_cake("fancy")
fancy_cake.describe()
```
