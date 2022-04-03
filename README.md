# Desafio1Borbotones
 Shortest path problem

Para ejecturar el programa solo es necesario correr el archivo .py estando este en el mismo directorio que el archivo "pesos.txt".

PONER LINK VIDEO

Problema

En este trabajo se analiza el problema del camino más corto (shortest path problem) para poder aplicarle algoritmos de búsqueda en función de encontrar soluciones. El problema consiste en poder trazar la ruta más corta desde una ciudad inicial hasta una ciudad final pasando a través de ciudades intermedias en el mapa. Esta ruta puede tener en cuenta las distancias entre cada ciudad para optimizar la cantidad de kilometros recorrida en el camino. De manera que el archivo de entrada tiene la lista de ciudades que componen el grafo, la ciudad por la que se parte el camino (punto inicial), la ciudad en donde termina el camino (punto final) y dos matrices: La primera con los caminos posibles desde una ciudad (correspondiendo una fila a su número en el arreglo) a otra y su distancia, mientras que la segunda contiene las distancias en línea recta desde cada ciudad a las otras (independiente de si existen caminos o no).

Solución propuesta

Se tendrán dos soluciones para este problema, una de las cuales ser será una búsqueda no informada (Búsqueda en anchura)y la otra será una búsqueda informada con una heurística admisible(A*). 
En el caso de la búsqueda en anchura, utilizamos este método en contraposición de la búsqueda en profundidad, debido a que esta última explora a fondo una rama del árbol de búsqueda, encontrando una solución; pero en el mayor de los casos, esta sería la menos intuitiva e ineficiente. Debido a esto, y que la solución es más probable que se encuentre en en niveles superficiales del árbol de búsqueda,  la anchura debe ser nuestra solución para las búsquedas desinformadas.

Se entiende que se ocupa dos métodos para medir la eficiencia de la heurística, porque si el algoritmo que la emplea resulta tener un desempeño igual o peor de la búsqueda en anchura, entonces se está en presencia de una pésima heurística y el curso de acción a seguir sería mejorarla tomando en cuenta el problema y la razón de su paupérrimo.

Ahora, cuando se tiene en cuenta la información del problema y se plantea una heurística admisible, es que se elige A* por sobre los demás candidatos. Este algorito es capaz de superar con creces a sus algoritmos competidores en solucionar la problemática expuesta, dado que su característica principal  es que la primera solución final que encuentra es una óptima (gracias a que la heurística admisible considerará siempre una solución igual o mejor que la existente), dejando a los demás algoritmos como opciones obsoletas.
