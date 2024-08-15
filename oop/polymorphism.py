class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

# for pet in [niko, felix]:
#     print(type(pet))
#     print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)
