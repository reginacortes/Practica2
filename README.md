# Practica2 : Recursión

## Problema

Un centro de distribucion de Correos de Mexico requiere planificar la recoleccion de paquetes que hara un agente postal en diferentes oficinas de correos en diferentes dıas de la semana. Para esto, cuenta con un mapa de recoleccion por dıa de la semana y peso de los paquetes a recolecta en cada oficina. En esta practica se desarrollará un programa que indicará las rutas que debera tomar el agente para hacer un recorrido optimo y cuanto peso recogera en total para decidir que vehıculo utilizar. 
La entrada será un archivo de texto con los mapas de las rutas a seguir en cada dıa de la semana. 

Cada lınea representara un mapa en formato de arbol que se explicara en clase en el que las hojas contaran con el peso a recolectar en cada oficina. El nodo raiz del arbol es el centro
de distribucion y las hojas son oficinas de correos en las que se indicara el peso a recolectar mediante un numero natural de uno o dos dıgitos. El numero de oficinas a visitar esta en el rango de 1 a 255. 

Se implementarán dos versiones de este programa:
- Versión Iterativa
- Version Recursiva

Salida: Una lınea de texto por cada dıa de las semana que diga: Ruta seguida, numero de calles visitadas y peso total

## Metodología

Observamos que cada línea del archivo es un mapa completo y se contituye un árbol completo para cada día de la semana. Por lo que se debe leer la línea que representa el mapa en formato de árbol y apartir de ésta, contruir dicho árbol para poder recorrerlo y arrojar el número de calles visitadas, la ruta seguida y el peso recolectado. 

Versión Iterativa



