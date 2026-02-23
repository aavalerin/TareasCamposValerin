import Metodo2
import random
import string
import pytest

# Codigos de retorno esperados
# Caso de éxito => 0

# Errores esperados metodo filtrar_vocales
# Error en caso de que cadena no sea un string => -100
# Error en caso de que cadena posea algo distinto a letras del abecedario => -200
# Error en caso de que cadena sea un string vacío => -300
# Error en caso de que cadena sea mayor a 30 caracteres => -400
# Error en caso de que bandera no sea un booleano => -500

# Errores esperados metodo encontrar_extremos
# Error en caso de que el parámetro no sea una lista => -600
# Error en caso de que la lista contenga elementos no numéricos => -700
# Error en caso de que la lista esté vacía => -800
# Error en caso de que la lista tenga más de 15 elementos => -900

# Prueba 3
# Verifica los casos de error de encontrar_extremos
def test_casos_error_encontrar_extremos():
    # Error si no es una lista
    estado, minimo, maximo = Metodo2.encontrar_extremos("no es lista")
    assert estado == -600
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = Metodo2.encontrar_extremos(123)
    assert estado == -600
    assert minimo is None
    assert maximo is None

    # Error si contiene elementos no numéricos
    estado, minimo, maximo = Metodo2.encontrar_extremos([1, 2, "3", 4])
    assert estado == -700
    assert minimo is None
    assert maximo is None

    estado, minimo, maximo = Metodo2.encontrar_extremos([1, 2, True, 4])
    assert estado == -700
    assert minimo is None
    assert maximo is None

    # Error si la lista está vacía
    estado, minimo, maximo = Metodo2.encontrar_extremos([])
    assert estado == -800
    assert minimo is None
    assert maximo is None

    # Error si la lista tiene más de 15 elementos
    lista_larga = list(range(16))
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_larga)
    assert estado == -900
    assert minimo is None
    assert maximo is None


# Prueba 4
# Verifica los casos de éxito de encontrar_extremos
def test_casos_exito_encontrar_extremos():
    # Caso con enteros positivos
    lista_prueba = [5, 2, 8, 1, 9, 3]
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_prueba)
    assert estado == 0
    assert minimo == 1
    assert maximo == 9

    # Caso con números negativos
    lista_prueba = [-5, -2, -8, -1]
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_prueba)
    assert estado == 0
    assert minimo == -8
    assert maximo == -1

    # Caso con floats
    lista_prueba = [3.5, 1.2, 9.8, 2.1]
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_prueba)
    assert estado == 0
    assert minimo == 1.2
    assert maximo == 9.8

    # Caso con un solo elemento
    lista_prueba = [42]
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_prueba)
    assert estado == 0
    assert minimo == 42
    assert maximo == 42

    # Caso aleatorio
    lista_prueba = [random.randint(-100, 100) for _ in range(random.randint(2, 15))]
    esperado_min = min(lista_prueba)
    esperado_max = max(lista_prueba)
    estado, minimo, maximo = Metodo2.encontrar_extremos(lista_prueba)
    assert estado == 0
    assert minimo == esperado_min
    assert maximo == esperado_max
