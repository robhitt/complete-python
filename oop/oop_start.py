class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    # Available as Dog.species or my_dog.species
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f"WOOF! My name is {self.name}")


print("=====================================")
my_dog = Dog("Lab", 'Sammy')
print(my_dog.bark())

