# WITH -> É UM GERENCIADOR DE CONTEXTO.

arquivo = open('notas.txt', 'w')
arquivo.write('Esta é uma anotação especial!')
arquivo.close()

with open('notas.txt', 'w') as arquivo:
    arquivo.write('Esta é uma anotação especial!')

print('Arquivo foi fechado')

import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print(f'Diretório temporário criado: {temp_dir}')
    input()