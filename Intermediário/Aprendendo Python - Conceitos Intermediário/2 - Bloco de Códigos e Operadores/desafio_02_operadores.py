# Desafio 02

# Temos duas funções abaixo que simulam operações
# em bancos de dados:
# - busca_dados, que retorna informação de um banco de dados,
# mas que falha 50% das vezes em que é executada.
# - processa_dados, que processa a informação obtida a partir do banco de dados.

# Você consegue usar os operadores e expressões que aprendemos
# para simplificar o bloco de código ao final do script?
# (Não modifique o corpo das funções)

import random

def busca_dados():
    if random.random() > 0.5:
        return None
    return 'xxxxx'

def processa_dados(dados):
    return f'Dados "{dados}" foram processados'

dados_banco = busca_dados()
if dados_banco is not None:
    dados_processados = processa_dados(dados_banco)
else:
    dados_processados = 'N/A'


if (dados_banco := busca_dados()) is not None:
    dados_processados = processa_dados(dados_banco)
else:
    dados_processados = 'N/A'

dados_processados = (
    processa_dados(dados_banco)
    if (dados_banco := busca_dados()) is not None
    else 'N/A'
)

print(f'Resultado: {dados_processados}')