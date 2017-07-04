## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        ## Instance of Dog has-a name attribute
        self.name = name

## Cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ## Instance of Cat has-a name attribute
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Instance of Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def _init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Instance of Employee has a salary
        self.salary = salary

## Fish is-s object
class Fish (object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## spot is-a Cat
spot = Cat("Spot")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet(spot)
mary.pet = spot

## frank is-a Employee, has-a salary(120000)
frank = Employee("Frank", 120000)

## frank has-a pet(rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
