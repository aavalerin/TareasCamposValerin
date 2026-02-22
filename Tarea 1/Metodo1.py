#Microcontroladores y Microprocesadores
#Sebastián Campos y Aarón Valerín


def filtrar_vocales(cadena, bandera):

    if not isinstance(cadena, str):
        return -100, None

    if len(cadena) == 0:
        return -300, None

    if not cadena.isalpha():
        return -200, None

    if len(cadena) > 30:
        return -400, None

    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"
    resultado = ""

    if bandera:
        for letra in cadena:
            if letra in vocales:
                resultado += letra
    else:
        for letra in cadena:
            if letra not in vocales:
                resultado += letra

    return 0, resultado
