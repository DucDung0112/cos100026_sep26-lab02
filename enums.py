class Pet:
    def __init__(self, name, age, sex, breed):
        self.name = name
        self.age = age
        self.sex = sex
        self.breed = breed


class Dog(Pet):
    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.sex}, and is a {self.breed}."


class Cat(Pet):
    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.sex}, and is a {self.breed}."


Dog1 = Dog("Mr. Woofers", 4, "Male", "dalmation")
Dog2 = Dog("Jobs", 8, "Male", "dachshund")
Cat1 = Cat("whiskers", 2, "Female", "siamese")

print(Dog1)
print(Dog2)
print(Cat1)