"""Type, Comprensión de Listas, Sorted y Filter."""
print("------------------Aca empieza el codigo--------------------------------")

from typing import List, Union
"""Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
"""

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    listafinal=[]
    for elemento in lista:
       if type(elemento) == str:
           listafinal.append(elemento)
    for elemento in lista:
        if type(elemento) == int:
           listafinal.append(elemento)
    return listafinal


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################
"""Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
"""

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    
    listafinal_1= [elemento for elemento in lista if type(elemento)== str]
    listafinal_2= [elemento for elemento in lista if type(elemento)== int]
    listafinal_1.extend(listafinal_2)
    return listafinal_1

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
# Con comprensión de listas
