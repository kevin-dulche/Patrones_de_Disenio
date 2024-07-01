# Prototype

## Definición del Patrón

El patrón Prototype especifica los tipos de objetos a crear utilizando una instancia prototípica y crea nuevos objetos copiando este prototipo.

## Problema que Resuelve

Cuando la creación de nuevos objetos es un proceso costoso (por ejemplo, cuando requiere muchas operaciones complejas, inicialización con datos pesados, o requiere acceso a recursos externos), el patrón Prototype permite clonar un objeto existente en lugar de crear una nueva instancia desde cero. Esto puede mejorar el rendimiento y la eficiencia de la aplicación.

## Estructura

1. **Prototype (Prototipo)**: Declara una interfaz para clonar a sí mismo.
2. **ConcretePrototype (Prototipo Concreto)**: Implementa la operación de clonación.
3. **Client (Cliente)**: Crea nuevos objetos solicitando a los prototipos que se clonen a sí mismos.

## Ventajas

* **Reducción de costos**: Evita la creación de objetos costosos desde cero al clonar objetos existentes.
* **Flexibilidad**: Permite añadir y quitar propiedades a las copias sin afectar al prototipo original.
* **Simplicidad**: Simplifica el proceso de creación de nuevos objetos complejos.

## Desventajas

* **Reducción de costos**: Evita la creación de objetos costosos desde cero al clonar objetos existentes.
* **Flexibilidad**: Permite añadir y quitar propiedades a las copias sin afectar al prototipo original.
* **Simplicidad**: Simplifica el proceso de creación de nuevos objetos complejos.

## Conclusiones

En resumen, el patrón Prototype es una herramienta poderosa para crear nuevos objetos de manera eficiente y flexible al copiar instancias existentes. Este patrón es especialmente útil en escenarios donde la creación de objetos es costosa en términos de recursos o tiempo.