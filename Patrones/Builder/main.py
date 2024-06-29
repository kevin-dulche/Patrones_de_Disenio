from cook import Cook
from pizza_builder import MargheritaBuilder

cook = Cook()
margherita_builder = MargheritaBuilder()
cook.make_pizza(margherita_builder)
pizza = cook.make_pizza(margherita_builder)
print(pizza)