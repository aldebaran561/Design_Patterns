# Design Patterns in PYTHON

## Table of Contents

- [What are Design Patterns](#what)
- [Uses of Design Patterns](#uses)
- [Types of Design Patterns](#types)
- [Some Explained Patterns](#some)
    - Creational Patterns
        - Builder Pattern
        - Singleton Pattern
        - Factory Pattern
        - Abstract Pattern
    - Structural Patterns
        - Adapter Pattern
        - Decorator Pattern
        - Facade Pattern
    - Behavioral Patterns
        - Iterator Pattern
        - Observer Pattern
        - Strategy Pattern
- [Criticism to Design Patterns](#critics)


## What are Design Patterns <a name="what"></a>

In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.

In other words, each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice.

## Uses of Design Patterns <a name="uses"></a>

Design patterns can speed up the development process by providing tested, proven development paradigms. Effective software design requires considering issues that may not become visible until later in the implementation. Reusing design patterns helps to prevent subtle issues that can cause major problems and improves code readability for coders and architects familiar with the patterns. Design patterns provide general solutions, documented in a format that doesn't require specifics tied to a particular problem. 

It is important to clarify this patterns are not *bulletproof* and just provides better ways to solve code issues.

## Types of Design Patterns <a name="types"></a>

There are three types of design patterns:

- Creational Design Patterns: These design patterns are all about **Class instantiation**. This pattern can be further divided into class-creation patterns and object-creational patterns. While class-creation patterns use inheritance effectively in the instantiation process, object-creation patterns use delegation effectively to get the job done.

- Structural Design Patterns: These design patterns are all about **Class and Object composition**. Structural class-creation patterns use inheritance to compose interfaces. Structural object-patterns define ways to compose objects to obtain new functionality.

- Behavioral Design Patterns: These design patterns are all about **Class's objects communication**. Behavioral patterns are those patterns that are most specifically concerned with communication between objects.

## Some Explained Patterns <a name="some"></a>

1. **Creationals Paterns:**

    1. **Builder Pattern:** Think about a class ```House```, which is a basic object with floor, walls and a roof. At this point is simple to think there are tons of kind of houses, like a house with garden, house with garage or house with pool. With Inheritance Pillar we can create as much sub-classes as we need, but this would be a problem if we need dozens and dozens of type of houses.
    
    **Solution**: Separate the construction of a complex object from its representation so that the same construction process can create different representations.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/builder/solution1.png)

    Pros:
        - You can build objects step by step, defer construction steps, or run steps recursively.
        - You can reuse the same building code when building multiple product renderings.
        - You can isolate a complex build code from the business logic of the product (Single Responsibility Principle)
    
    Cons
        - Complex of code increases because pattern demand the creation of new classes.
      
    2. **Singleton Pattern:** Application needs one, and only one, instance of an object. Additionally, lazy initialization and global access are necessary.
    
    **Solution**: Ensure a class has only one instance, and provide a global point of access to it. Also, encapsulated "just-in-time initialization" or "initialization on first use".
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/singleton/structure-es.png)
    
    Pros: 
    
        - You can be sure that a class has only one instance.
        - You get a global access point to that instance.
        - The Singleton object is only initialized when it is first required.
    
    Cons:
    
        - It violates the Simple Responsibility Principle (SRP). The pattern solves two problems at the same time.
        - The Singleton pattern can mask poor design, for example when program components know too much about each other.

    3. **Factory Pattern**: If your code is too overfitted, this just will be applied to a kind of object. In other words, if you have a logistic software who are just defined for ground transportation, what happend if the owner wants to apply the business logic to marine transportation. OBviously this will crash the code.
    
    **Solution**: Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses. Define a *"Virtual Constructor"*. This pattern is highly correlated with Inheritance Pillar.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/factory-method/solution1.png)
    
    Pros:
    
        - You avoid high coupling between the creator and the specific products.
        - Single Responsibility Principle (SRP). You can move the product build code to a place in the program, making the code easier to maintain.
        - Open/Close Principle. You can incorporate new types of products into the program without breaking down the existing client code.
    
    Cons: 
        
        - The code can be complicated, as you must incorporate a multitude of new sub-classes to implement the pattern.
    
    4. **Abstract Pattern**: If an application is to be portable, it needs to encapsulate platform dependencies. These "platforms" might include: windowing system, operating system, database, etc. Too often, this encapsulation is not engineered in advance, and lots of case statements with options for all currently supported platforms begin to procreate like rabbits throughout the code.
    
    **Solution**: Provide an interface for creating families of related or dependent objects without specifying their concrete classes. A hierarchy that encapsulates: many possible "platforms", and the construction of a suite of "products".
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1.png)
    
    Pros:
    
        - You can be sure that the products you get from a factory are compatible with each other.
        - You avoid a high coupling between specific products and the client code.
        - Single Responsibility Principle (SRP). You can move the product build code to a place in the program, making the code easier to maintain.
        - Open/Close Principle. You can incorporate new types of products into the program without breaking down the existing client code.

    Cons:
    
        - It may be that the code is more complicated than it should, as many new interfaces and classes are introduced alongside the pattern.
    
    
2. **Structurals Patterns:**

    1. **Adapter Pattern**: Imagine you are working with an app who measure miles driven by a car. You don't have access to the source code and you need to convert the result into kms. 
    
    **Solution**: Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces. Wrap an existing class with a new interface. Impedance match an old component to a new system.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/adapter/solution-es.png)

    Pros:
    
        - Single Responsibility Principle (SRP). You can separate the interface or the data conversion code from the primary business logic of the program.
        - Open/Close Principle. You can introduce new types of adapters to the program without breaking down the existing client code, as long as they work with the adapters through the client interface.

    Cons:
    
        - The overall complexity of the code increases as you have to introduce a group of new interfaces and classes. Sometimes it's easier to change the service class to match the rest of your code.

    2. **Decorator Pattern**:
    
    **Solution**:Attach additional responsibilities to an object dynamically. In other words this is a Dynamic Inheritance which prevents you to create dozens of classes. Decorators provide a flexible alternative to subclassing for extending functionality. Client-specified embellishment of a core object by recursively wrapping it. Wrapping a gift, putting it in a box, and wrapping the box.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/decorator/problem3.png)
    
    Pros:
    
        - You can extend the behavior of an object without creating a new subclass.
        - You can add or remove responsibilities from an object during runtime.
        - You can combine multiple behaviors by wrapping an object with multiple decorators.
        - Single Responsibility Principle (SRP). You can divide a monolithic class that implements many possible variants of behavior, into several smaller classes.
        
    Cons:
    
        - It is difficult to implement a decorator in such a way that its behavior does not depend on the order in the decorator stack.
        - Layers' initial setup code can look nasty.
       
    3. **Facade Pattern**: A segment of the client community needs a simplified interface to the overall functionality of a complex subsystem.
    
    **Solution**: Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use. Wrap a complicated subsystem with a simpler interface.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/facade/example.png)
    
    Pros:
    
        - You can isolate your code from the complexity of a subsystem.
        
    Cons:
    
        - A facade can become an all-powerful object attached to all the classes of an application.
        
        
3. **Behavioral Patterns**:

    1. **Iterator Pattern**:Need to "abstract" the traversal of wildly different data structures so that algorithms can be defined that are capable of interfacing with each transparently.
    
    **Solution**: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/iterator/solution1.png?id=2f5fbcce6099d8ea09b2)

    Pros:
    
        - Single Responsibility Principle (SRP). You can clean up client code and collections by extracting bulky traversal algorithms and placing them in separate classes.
        - Open/Close Principle (OCP). You can implement new types of collections and iterators and pass them to existing code without breaking anything.
        - You can loop through the same collection in parallel because each iterator object contains its own iteration state.
        
    Cons:
    
        - Applying the pattern can be overkill if your application works only with simple collections.

    2. **Observer Pattern**: A large monolithic design does not scale well as new graphing or monitoring requirements are levied. In other words, not all the clients of the app want notifications about certain things of the app, so let them to susbcribe to the service they really want.
    
    **Solution**: 
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/observer/solution1-es.png?id=3bcc13f74ff9ed564c42)
    
    Pros:
    
        - Open/Close Principle (OCP). You can introduce new subscriber classes without having to change the code of the notifier (and vice versa if there is a notifier interface).
        - You can establish relationships between objects at runtime.
        
    Cons:
    
        - Subscribers are notified in a random order.

    3. **Strategy Pattern**: There are common situations when classes differ only in their behavior.
    
    **Solution**: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from the clients that use it. Capture the abstraction in an interface, bury implementation details in derived classes.
    
    ![Ejemplo](https://refactoring.guru/images/patterns/diagrams/strategy/solution.png)
    
    Pros:
    
        - You can exchange algorithms used within an object during runtime.
        - You can isolate the implementation details of an algorithm from the code that uses it.
        - You can substitute inheritance for composition.
        
    Cons:
    
        - If you only have a couple of algorithms that rarely change, there is no real reason to overcomplicate the program with new classes and interfaces that come with the pattern.
        - Clients must know the differences between strategies in order to select the right one.
        
        
 
 

 


## Criticism to Design Patterns <a name="critics"></a>

The concept of design patterns has been criticized by some in the field of computer science.

### Targets the wrong problem

The need for patterns results from using computer languages or techniques with insufficient abstraction ability. Under ideal factoring, a concept should not be copied, but merely referenced. But if something is referenced instead of copied, then there is no "pattern" to label and catalog.


### Lacks formal foundations

The study of design patterns has been excessively ad hoc, and some have argued that the concept sorely needs to be put on a more formal footing. At OOPSLA 1999, the Gang of Four were (with their full cooperation) subjected to a show trial, in which they were "charged" with numerous crimes against computer science. They were "convicted" by ⅔ of the "jurors" who attended the trial.

### Leads to inefficient solutions

The idea of a design pattern is an attempt to standardize what are already accepted best practices. In principle this might appear to be beneficial, but in practice it often results in the unnecessary duplication of code. It is almost always a more efficient solution to use a well-factored implementation rather than a "just barely good enough" design pattern.

### Does not differ significantly from other abstractions

Some authors allege that design patterns don't differ significantly from other forms of abstraction, and that the use of new terminology (borrowed from the architecture community) to describe existing phenomena in the field of programming is unnecessary. The Model-View-Controller paradigm is touted as an example of a "pattern" which predates the concept of "design patterns" by several years. It is further argued by some that the primary contribution of the Design Patterns community (and the Gang of Four book) was the use of Alexander's pattern language as a form of documentation; a practice which is often ignored in the literature.
