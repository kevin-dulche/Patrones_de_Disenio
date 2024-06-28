from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        self.__model = model

    def deliver(self):
        return f"Auto {self.__model} entregado"

class Truck(Vehicle):
    def __init__(self, model):
        self.__model = model

    def deliver(self):
        return f"Camion {self.__model} entregado"
