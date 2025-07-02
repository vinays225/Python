class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Output: Bark
animal_sound(Cat())  # Output: Meow
