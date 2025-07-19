# Desafio 03

# Meus amigos possuem os seguintes interesses:

# Gostam de programação: Ricardo, Roberto, Pedro, Vinicius
# Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinicius
# Estudam na Asimov Academy: Ricardo, Mateus, Paulo, Pedro

# Usando operações de conjunto, encontre o conjunto
# de amigos que gostam de programação e estudam na
# Asimov Academy, mas que não gostam de jogar futebol.

gostam_de_programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
gostam_futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
estudam_asimov = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

R = gostam_de_programacao.intersection(estudam_asimov).difference(gostam_futebol)
Y = (gostam_de_programacao | estudam_asimov) - gostam_futebol
print(R)
print(Y)