from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined

    def years_on_platform(self):
        return 2025 - self.year_joined

    @abstractmethod
    def show_role(self):
        pass


class Customer(User):
    def show_role(self):
        return "Customer"

    def __str__(self):
        return f"{self.name} ({self.show_role()}) - Using platform for {self.years_on_platform()} years."


class Vendor(User):
    def show_role(self):
        return "Vendor"

    def __str__(self):
        return f"{self.name} ({self.show_role()}) - Using platform for {self.years_on_platform()} years."




