# Desafio 01
import itertools

# Crie uma função que retorna os valores de duas listas
# de forma intercalada, mesmo quando as listas têm tamanho
# diferente. Por exemplo, dadas as listas.

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']

# A função deve retornar:

[1, 'a', 2, 'b', 3, 'c', 'd', 'e']

import itertools

def retorna_intercalado(lista1, lista2):
    resultado = []
    for valor1, valor2 in itertools.zip_longest(lista1, lista2):
        if valor1 is not None:
            resultado.append(valor1)
        if valor2 is not None:
            resultado.append(valor2)
    return resultado

print(retorna_intercalado(L1, L2))