"""Expresiones Booleanas."""
print("------------------Aca empieza el codigo---------------------------------")
"""Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricciónes:
        - Utilizar un if para cada posibilidad.
        - Utilizar la función lower() sólo una vez.
        - No utilizar ELSE.
        - Utilizar 6 returns.

    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
"""
def es_vocal_if(letra: str) -> bool:
    string = str.lower(letra)
    if string == "a":
        return True
    if string == "e":
        return True
    if string == "i":
        return True
    if string == "o":
        return True
    if string == "u":
        return True
    return False

# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
assert es_vocal_if("e")
assert es_vocal_if("E")
# NO MODIFICAR - FIN


###############################################################################

"""Re-escribir utilizando un sólo IF y el operador IN.

    Restricciónes:
        - Utilizar un único IF.
        - Utilizar dos returns.
        - No utilizar ELSE.
        - No utilizar FOR.
        - No utilizar listas.

    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations # noqa: E501
"""
def es_vocal_if_in(letra: str) -> bool:
    string = str.lower(letra)
    for x in string:
        if x == "a":
            return True
        if x == "e":
            return True
        if x == "i":
            return True
        if x == "o":
            return True
        if x == "u":
            return True
        return False

# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################
"""
    Re-escribir como expresión booleana utilizando el operador IN

Restricciónes:
    - No utilizar IF.
    - Utilizar un único return.
    - No utilizar FOR.
    - No utilizar listas.
"""
def es_vocal_in(letra: str) -> bool:



# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
