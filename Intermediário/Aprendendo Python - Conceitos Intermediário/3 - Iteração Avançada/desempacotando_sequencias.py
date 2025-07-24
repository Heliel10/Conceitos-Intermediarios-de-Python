## 3.2 DESEMPACOTANDO SEQUÊNCIAS

seq = (10, 20, 30)
a, b, c = seq
a
b
c

dic = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
}

for chave, valor in dic.items():
    print(chave, valor)

nomes = ['Juliano', 'Laura', 'Roberto', 'Guilherme']
idades = [30, 24, 19, 47]

for elemento in enumerate(zip(nomes, idades)):
    print(elemento)

for i, (nome, idade) in enumerate(zip(nomes, idades)):
    print(i, nome, idade)


minha_lista = [1, 2, 3, 4, 5]
primeiro, *meio, ultimo = minha_lista
primeiro
ultimo
meio

primeiro, segundo, *resto = (1, 2, 3, 4)
primeiro
resto
segundo

*resto, penultimo, ultimo = (1, 2, 3, 4)
resto
penultimo
ultimo


primeiro, *meio, ultimo = (1, 2)
primeiro
meio
ultimo

primeiro, *_, ultimo = (1, 2, 3, 4)
primeiro
_
ultimo