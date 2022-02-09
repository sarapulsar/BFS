# PROBLEMA 1. TEORIA DE LOS SEIS GRADOS

Descripción:1. La teoría de los seis grados de separación dice que una persona podría conocer a cualquier
otra persona del mundo siguiendo una cadena de personas que se conocen entre si de tamaño
máximo  6. Suponiendo que si una persona conoce a otra,  entonces tienen una relación de
amistad en la red social Facebook, diseñar un algoritmo lo más eficiente posible, que reciba la
base de datos de relaciones de amistad de esta red social y determine si la teoria de los seis
grados de separación se cumple.

_Con esta implementación se intenta comprobar la teoria de los seis grados, el problema señala que la entradas pueden ser una lista de personas de n cantidad y su salida las relaciones que puedan existir (enlaces,aristas).Para la solución ejercicio se hace uso del recorrido Breadth First Search._

## ¿Cómo funciona el Programa'

1. _Se toma de referencia un generador de pruebas que crea un archivo .txt, donde se almacena información. Para este ejercicio se considera como base de datos con información de las relaciones de Facebook. A partir de este archivo se logra generar un diccionario, que sirve como entrada para mi programa. También se considera un grafo no dirgido_
2. _Se obtiene una lista de adyacencias que permite conocer las relaciones que se tienen, donde key corresponde al vertice y val a los adyacentes a el._ 
3. _Finalmente se realiza recorrido por BFS (Breadth First Search) donde se obtiene el nivel y el recorrido que se hizo a los vertices desde un nodo raiz (siempre se toma el primero que se genere en la columnna y fila del diccionario._
4. _El programa arroja si se puedo comprobar o no la teoria mencionada._
5._El programa se desarrolla en Python._

## Ejemplo de solución

![image](https://user-images.githubusercontent.com/8904232/153096575-2589e2d7-f0dd-4747-855e-02f62d4b61bc.png)





