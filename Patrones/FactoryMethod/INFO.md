# Factory Method

## Definición del Patrón

El patrón Factory Method define una interfaz para crear un objeto, pero permite que las subclases decidan qué clase instanciar. De esta manera, el patrón delega el proceso de creación a las subclases.

## Problema que Resuelve
En muchos casos, las aplicaciones necesitan crear objetos de diversas clases derivadas de una clase base común. Si el código de creación de estos objetos está incrustado en la aplicación, resulta difícil agregar nuevas clases derivadas sin modificar el código existente. Esto rompe el principio de abierto/cerrado (Open/Closed Principle) de SOLID, que establece que las clases deben estar abiertas a la extensión pero cerradas a la modificación.

## Estructura

1. **Product (Producto)**: Define la interfaz de los objetos que el método de fábrica crea.
2. **ConcreteProduct (Producto Concreto)**: Implementa la interfaz Product.
3. **Creator (Creador)**: Declara el método de fábrica, que devuelve un objeto de tipo Product. Creator puede también definir una implementación predeterminada del Factory Method.
4. **ConcreteCreator (Creador Concreto)**: Sobrescribe el método de fábrica para devolver una instancia de ConcreteProduct.

## Ventajas

* **Fomenta la reutilización**: Permite utilizar código ya existente sin necesidad de modificarlo.
* **Facilita la extensión**: Añadir nuevos productos es sencillo y no afecta al código existente.
* **Reducción de acoplamiento**: Los creadores y productos están desacoplados.

## Desventajas

* **Complejidad**: Introduce más clases y hace el diseño más complejo.
* **Sobrecarga**: En algunos casos, el uso de Factory Method puede parecer excesivo para problemas simples.

## Uso

En resumen, el patrón Factory Method es una herramienta poderosa para manejar la creación de objetos en sistemas que requieren flexibilidad y extensibilidad, permitiendo que las subclases decidan qué instancias concretas deben ser creadas.