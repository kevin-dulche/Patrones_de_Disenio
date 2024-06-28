# Singleton

## Definición del Patrón

El patrón Singleton asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.

## Problema que Resuelve

En muchas situaciones, es deseable que una clase tenga exactamente una instancia en toda la aplicación. Por ejemplo, puede ser útil tener una única conexión a una base de datos compartida o un registro de eventos centralizado. Además, el patrón Singleton garantiza que la instancia sea creada bajo demanda y que siempre se devuelva la misma instancia cada vez que se solicite.

## Estructura

1. Singleton: Define una operación estática para acceder a la única instancia, que se asegura de que solo se crea una vez.

## Ventajas

* **Control de acceso único**: Garantiza que solo haya una instancia de la clase y proporciona un punto de acceso global a ella.
* **Ahorro de recursos**: Evita la creación de múltiples instancias si no son necesarias.

## Desventajas

* **Puede introducir acoplamiento global**: El acceso global a la instancia puede dificultar las pruebas unitarias y la modularidad del código.
* **Puede ocultar dependencias**: Puede ser difícil detectar y corregir dependencias ocultas en el código.

## Uso

El patrón Singleton se usa comúnmente en situaciones donde necesitamos controlar el acceso a recursos compartidos, como bases de datos, registros de eventos, configuraciones de aplicación, entre otros. Es crucial usarlo con moderación y tener en cuenta sus implicaciones en el diseño y la arquitectura de software.