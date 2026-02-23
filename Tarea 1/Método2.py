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
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # c. Verificar que no esté vacía
    if len(lista_numeros) == 0:
        return -800, None, None

    # d. Verificar que no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return -900, None, None

    # b. Verificar que todos sean números (int o float)
    for elemento in lista_numeros:
        if not isinstance(elemento, (int, float)):
            return -700, None, None

    # e. Encontrar mínimo y máximo
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    # f. Retornar código de éxito + valores
    return 0, minimo, maximo
