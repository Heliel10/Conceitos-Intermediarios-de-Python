# Desafio 02

import itertools

# Imagine que você tem um restaurante com
# os seguintes itens no seu menu:

comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90,
}

bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90,
}

entradas = {
    'Batata Frita': 12,
    'Picadinho': 15,
}

# Crie um novo dicionário chamado de combos,
# onde cada chave é uma tupla contendo (comida, bebida),
# e o seu respectivo valor é o preço daquela combinação
# de comida e bebida.

combo = {}

#for chave_combo in itertools.product(comidas, bebidas):
    #chave_comida, chave_bebida = chave_combo
    #preco_combo = comidas[chave_comida] + bebidas[chave_bebida]
    #combo[chave_combo] = round(preco_combo, 2)

#print(combo)

#for chave_comida, preco_comida in comidas.items():
    #for chave_bebida, preco_bebida in bebidas.items():
        #chave_combo = (chave_comida, chave_bebida)
        #preco_combo = preco_comida + preco_bebida
        #combo[chave_combo] = round(preco_combo, 2)

for tupla in itertools.product(comidas.items(), bebidas.items(), entradas.items()):
    chave_combo = tuple(tup[0] for tup in tupla)
    preco_combo = sum(tup[1] for tup in tupla)
    combo[chave_combo] = round(preco_combo, 2)

print(combo)