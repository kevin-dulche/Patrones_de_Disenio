import copy
from prototype import Prototype

class SystemConfigPrototype(Prototype):
    def __init__(self, configuration : dict) -> None:
        self.configuration = configuration

    def clone(self) -> Prototype:
        return copy.deepcopy(self)