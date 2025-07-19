op = 1

if op == 1:
    print('Opção 1')
elif op == 2:
    print('Opção 2')
else:
    print('Opção inválida!')

notas = {
    'João': 10,
    'Maria': 9,
    'Mateus': 9.2,
}

match notas:
    case {'João': 10}:
        print('João tirou nota 10!')
    case _:
        print('Nenhuma informação obtida!')