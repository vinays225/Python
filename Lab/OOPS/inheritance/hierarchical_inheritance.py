class Parent:
    def display(self):
        print("Common method")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.display()
c2.display()
