from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} with Credit Card.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

payment = UPI()
payment.pay(500)
