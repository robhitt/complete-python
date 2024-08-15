class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # def who_am_i(self):
    #     print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF!")


# my_animal.who_am_i()
# my_animal.eat()
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

