"""For, Sum, Reduce."""

print("------------------Aca empieza el codigo--------------------------------")

def sumatoria_basico(n: int) -> int:
    suma = 0
    for x in range(n+1):
        suma += x
    return suma
    
"""Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
"""


# NO MODIFICAR - INICIO

assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

"""Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
"""

def sumatoria_sum(n: int) -> int:
    list=range(n+1)
    return sum(list)
    



# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402
"""Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
"""

def multiplicar_basico(numeros: Iterable[float]) -> float: 
    total = 1
    if not numeros:
            total = 0
    for x in numeros:
        if numeros:
            total = total * x 
    return total

# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
