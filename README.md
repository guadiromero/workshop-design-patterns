# Design Patterns Workshop

## What are Design Patterns?

Design Patterns are reusable solutions to commonly occurring problems in software design. They are not ready-made solutions, but rather templates that we can customize to suit the specific needs of our program.

## Catalog of Design Patterns

Design Patterns can be classified as creational, structural or behavioral depending on their purpose. **Creational** patterns concern the process of object creation. **Structural** patterns deal with the composition of classes or objects. **Behavioral** patterns characterize the ways in which classes or objects interact and distribute responsibility.

| **Creational**   | **Structural** | **Behavioral**          |
|------------------|----------------|-------------------------|
| Builder          | Adapter        | Chain of Responsibility |
| Factory Method   | Bridge         | Command                 |
| Abstract Factory | Composite      | Interpreter             |
| Prototype        | Decorator      | Iterator                |
| Singleton        | Façade         | Mediator                |
|                  | Flyweight      | Memento                 |
|                  | Proxy          | Observer                |
|                  |                | State                   |
|                  |                | Strategy                |
|                  |                | Template Method         |
|                  |                | Visitor                 |

## Solid Principles

The SOLID principles were first promoted by Robert C. Martin (also known as Uncle Bob) in his [2000 paper](http://staff.cs.utu.fi/~jounsmed/doos_06/material/DesignPrinciplesAndPatterns.pdf), while the acronym was introduced some time later by Michael Feathers. They are a set of principles that guide the design of Object-Oriented Programming, and they provide the fundamental ideas behind Design patterns. Their aim is to make code more understandable, flexible and maintainable.

- **Single Responsibility Principle:** A class should do one thing and therefore it should have only a single reason to change.

- **Open/Closed Principle:** Classes should be open for extension (adding new functionality) and closed to modification (changing the code of an existing class).

- **Liskov Substitution Principle:** Subclasses should be substitutable for their base classes.

- **Interface Segregation Principle:** Clients should not be forced to depend upon interfaces that they do not use.

- **Dependency Inversion Principle:** Classes should depend upon interfaces or abstract classes instead of concrete classes and functions.

## How this workshop is structured

In this miniseries workshop, we will explore how to use Design Patterns to help us write better code. For each pattern, we will present:

- A simple code example where we do not use any patterns, and there is some issue that needs to be solved.

- The same code but using the selected pattern to solve that issue.

The examples are in Python, however, the principles are applicable to all Object-Oriented Programming.

## Useful resources

If you would like to dive deeper into this topic, you can try this [Udemy course](https://www.udemy.com/course/design-patterns-python/) that explains Design Patterns one by one with Python examples and hands-on exercises. You can also refer to the classic [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.goodreads.com/en/book/show/85009) book. This [online catalog](https://refactoring.guru/design-patterns/catalog) is also very handy when you are trying to apply the patterns in your daily work.