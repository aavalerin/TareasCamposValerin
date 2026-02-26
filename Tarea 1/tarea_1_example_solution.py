# Microcontroladores y Microprocesadores - Tarea 1
# Sebastián Campos y Aarón Valerín


def filtrar_vocales(cadena, bandera):
    """
    Retorna siempre dos valores:
    (codigo, resultado)

    Códigos:
     0     -> Éxito
    -100   -> Error: el parámetro cadena no es string
    -200   -> Error: la cadena contiene caracteres no alfabéticos
    -300   -> Error: la cadena está vacía
    -400   -> Error: la cadena tiene más de 30 caracteres
    -500   -> Error: el parámetro bandera no es booleano
    """

    # a. Verificar que cadena sea string
    if not isinstance(cadena, str):
        return -100, None

    # b. Verificar que no esté vacía
    if len(cadena) == 0:
        return -300, None

    # c. Verificar que solo contenga letras
    if not cadena.isalpha():
        return -200, None

    # d. Verificar que no tenga más de 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # e. Verificar que bandera sea booleano
    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"
    resultado = ""

    # f. Filtrar según el valor de bandera
    for letra in cadena:
        if bandera and letra in vocales:
            resultado += letra
        elif not bandera and letra not in vocales:
            resultado += letra

    return 0, resultado


def encontrar_extremos(lista_numeros):
    """
    Retorna siempre tres valores:
    (codigo, minimo, maximo)

    Códigos:
     0     -> Éxito
    -600   -> Error: el parámetro no es una lista
    -700   -> Error: la lista contiene elementos no numéricos
    -800   -> Error: la lista está vacía
    -900   -> Error: la lista tiene más de 15 elementos
    """

    # a. Verificar que sea lista
    if not isinstance(lista_numeros, list):.
        return -600, None, None

    # b. Verificar que no esté vacía
    if len(lista_numeros) == 0:
        return -800, None, None

    # c. Verificar que no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return -900, None, None

    # d. Verificar que todos sean números (int o float)
    for elemento in lista_numeros:
        if (not isinstance(elemento, (int, float))
            or isinstance(elemento, bool)):
            return -700, None, None

    # e. Encontrar mínimo y máximo
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return 0, minimo, maximo
