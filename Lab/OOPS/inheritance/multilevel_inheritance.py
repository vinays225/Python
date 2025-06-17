class Grandfather:
    def house(self):
        print("Owns a house")

class Father(Grandfather):
    def car(self):
        print("Owns a car")

class Son(Father):
    def bike(self):
        print("Owns a bike")

s = Son()
s.house()
s.car()
s.bike()
