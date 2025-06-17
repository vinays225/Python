class Employee:
    def __init__(self, name, salary):
        self.name = name           # public
        self.__salary = salary     # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

emp = Employee("Vinay", 50000)

print(emp.name)               # OK
print(emp.get_salary())       # OK

emp.set_salary(60000)
print(emp.get_salary())       # 60000

emp.set_salary(-100)          # Invalid salary
