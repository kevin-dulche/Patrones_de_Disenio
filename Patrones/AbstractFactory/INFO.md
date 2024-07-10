# Abstract Factory

## Definición del Patrón

El patrón Abstract Factory ofrece una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas. Permite que una clase delegue la responsabilidad de instanciar objetos a una clase específica que maneja la creación de objetos.

## Problema que resuelve

Cuando un sistema debe ser independiente de cómo se crean, componen y representan sus objetos, el patrón Abstract Factory permite crear familias de objetos relacionados sin acoplarse a sus clases concretas. Es especialmente útil cuando los productos deben ser usados juntos y son variantes de un conjunto general de productos.

## Estructura

1. **AbstractFactory (Fábrica Abstracta)**: Declara una interfaz para operaciones que crean productos abstractos.
2. **ConcreteFactory (Fábrica Concreta)**: Implementa las operaciones para crear objetos concretos.
3. **AbstractProduct (Producto Abstracto)**: Declara una interfaz para un tipo de producto objeto.
4. **Product (Producto Concreto)**: Define un objeto que implementa la interfaz de un producto abstracto.
5. **Client (Cliente)**: Utiliza únicamente las interfaces declaradas por AbstractFactory y AbstractProduct.

## Ventajas

* **Cohesión de familias de productos**: Garantiza que los productos creados son compatibles entre sí.
* **Desacoplamiento del cliente y las implementaciones concretas**: Permite que el cliente use productos sin conocer sus clases concretas.
* **Flexibilidad y extensibilidad**: Facilita la adición de nuevas familias de productos sin cambiar el código del cliente.

## Desventajas

* **Complejidad**: Introduce más clases y puede hacer el diseño más complejo.
* **Dificultad de soporte para nuevos tipos de productos**: Añadir un nuevo tipo de producto puede requerir cambios en todas las fábricas abstractas y concretas.

## Conclusiones

En resumen, el patrón Abstract Factory es una herramienta poderosa para crear familias de objetos relacionados de manera coherente y flexible, asegurando la compatibilidad entre los objetos creados y desacoplando el cliente de las implementaciones concretas.