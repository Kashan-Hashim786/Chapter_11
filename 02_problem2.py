class animal:
    pass

class pets(animal):
    pass

class Dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!")

dogObject = Dog()
dogObject.bark()