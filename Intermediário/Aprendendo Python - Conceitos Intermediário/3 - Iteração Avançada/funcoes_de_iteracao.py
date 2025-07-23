# enumerate
nomes = ['Juliano', 'José', 'Lucas', 'Luiza']

for i, nome in enumerate(nomes, 1):
    print(f'Posição da lista {i} -> Nome {nome}')

# sorted
conj = {1, 10, -1, 4}
ordenados = sorted(conj)
ordenados

# reversed
for i in reversed(range(10)):
    print(i)

# zip
nomes = ['Juliano', 'Laura', 'Roberto', 'Guilherme']
idades = [30, 24, 19, 47]
cpfs = ['xxx', 'yyy', 'zzz']
emails = ['juliano@empresa.com', 'laura@empresa.com']

for elemento in zip(nomes, idades, cpfs, emails):
    print(elemento)