class Father:
    def skill(self):
        print("Father is a carpenter")

class Mother:
    def hobby(self):
        print("Mother paints")

class Child(Father, Mother):
    def play(self):
        print("Child plays football")

c = Child()
c.skill()   # From Father
c.hobby()   # From Mother
