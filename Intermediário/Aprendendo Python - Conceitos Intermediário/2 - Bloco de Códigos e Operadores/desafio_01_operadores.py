# Desafio 01

# Crie uma função que retorna se um número inteiro n
# (maior que zero) é primo.

# Dica: um número primo é um número que só é divisivel por 1
# ou por ele mesmo.

def primo(n):
    if n <= 2:
        return True
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

for n in [1, 5, 10, 13, 15, 17]:
    print(f'Número {n} é primo? {primo(n)}')

