# OPERADOR TERNÁRIO (Outras linguagens)
## var = condição ? valor se verdadeiro ; valor se falso

# EXPRESSÃO CONDICIONAL (Python)
## var = valor_verdadeiro se condição senão valor_falso

x = 4
y = 5

if x > y:
    maior_valor = x
else:
    maior_valor = y

maior_valor



maior_valor = x if x > y else y
maior_valor

def pegar_cor(valor):
    return 'vermelho' if valor < 0 else 'azul'

for valor in [-1, 0, 1]:
    print(f'A cor do valor é {valor} é {pegar_cor(valor)}')



numeros = [1, 2, 3, 4]

pares_quadrados = [
    n ** 2
    if n % 2 == 0
    else n
    for n in numeros
]
pares_quadrados