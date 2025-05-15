# example of https://www.geeksforgeeks.org/bridge-design-pattern/ because book example is too convuluted

from abc import ABC, abstractmethod


class Workshop(ABC):

    @abstractmethod
    def work(self):
        pass


class Produce(Workshop):

    def work(self):
        return "Produced"


class Assemble(Workshop):

    def work(self):
        return "Assembled"

class Vehicle(ABC):

    def __init__(self, workshop_1: Workshop, workshop_2: Workshop):
        self._workshop_1 = workshop_1
        self._workshop_2 = workshop_2

    @abstractmethod
    def manufacture(self):
        pass


class Car(Vehicle):
    def __init__(self, workshop_1: Workshop, workshop_2: Workshop):
        super().__init__(workshop_1, workshop_2)

    def manufacture(self):
        print(f"Manufacture car")
        print(self._workshop_1.work())
        print(self._workshop_2.work())
        print("\n")


class Bike(Vehicle):
    def __init__(self, workshop_1: Workshop, workshop_2: Workshop):
        super().__init__(workshop_1, workshop_2)

    def manufacture(self):
        print(f"Manufacture bike")
        print(self._workshop_1.work())
        print(self._workshop_2.work())
        print("\n")

if __name__ == "__main__":
    car = Car(workshop_1=Produce(), workshop_2=Assemble())
    car.manufacture()

    bike = Bike(workshop_1=Produce(), workshop_2=Assemble())
    bike.manufacture()


