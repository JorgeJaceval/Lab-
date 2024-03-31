Alumnos: Joaquin Alonso Viveros Perez y Jorge Antonio Aceval Rojas
Rol: 202273586-4 y 202273513-9 respectivamente.
Paralelo: 201 y 200 respectivamente.

Especificación de los algoritmos y desarrollo:

Según lo visto en clases, a través del método del polinomio característico, pudimos realizar todas las conversiones.
Para esto, fue necesario manejar el número binario y hexadecimal de derecha hacia izquierda (Ejemplo 1010 / A), siendo su exponente su posición, y el número en cuestión el cual se multiplica (sea con un 2^n ó 16^n, según corresponda). Finalmente, luego de recorrer todo el número, se realizará una suma total, el cual corresponde a la conversión final de las coordenadas a decimal.
En particular, el cambio de base octal-decimal se hizo de izquierda hacia derecha siguiendo la misma idea de las posiciones con 8^n y el número respectivo, tal que n toma el valor del largo del número menos 1 desde la extrema izquierda hasta 0 en la extrema derecha.

Supuestos utilizados:

La tarea será revisada con la versión de Python más actualizada. Los inputs serán tal que, primero se elija la base y después se introduzca cada coordenada por separado (x e y).










