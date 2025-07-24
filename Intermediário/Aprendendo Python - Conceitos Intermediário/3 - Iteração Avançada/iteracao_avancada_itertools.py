## 3.3 - ITERAÇÃO AVANÇADA ITERTOOLS

import itertools

seq1 = (1, 2, 3)
seq2 = ['a', 'b', 'c']

for elemento in itertools.chain(seq1, seq2, seq2, seq2):
    print(elemento)

### itertools.zip_longest
nomes = ['Juliano', 'Laura', 'Roberto', 'Guilherme']
idades = [30, 24, 19, 47]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['juliano@empresa.com', 'laura@empresa.com']

for elemento in itertools.zip_longest(nomes, idades, cpfs, emails, fillvalue='???'):
    print(elemento)

### itertools.product
comidas = ['Churrasco', 'Pizza', 'Sushi']
bebidas = ('Refrigerante', 'Água')

for prato in itertools.product(comidas, bebidas):
    print(prato)

### itertools.combinations
nomes = ['Marcos', 'Lucas', 'Rodrigo', 'Carlos']

for comb in itertools.combinations(nomes, 2):
    print(comb)
for comb in itertools.permutations(nomes, 2):
    print(comb)
    input()

### itertools.cycle
nomes = ['Marcos', 'Lucas', 'Rodrigo', 'Carlos']
equipes = ['E1', 'E2']

for nome, equipe in zip(nomes, itertools.cycle(equipes)):
    print(nome, equipe)