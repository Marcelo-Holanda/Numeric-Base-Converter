num = int(input('Digite um número:'))
print('''Escolha uma das bases para conversção:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')

opção = int(input('Digite Sua opção:'))
if opção == 1:
    print('{} Convertido em BINÁRIO é igual á {}'.format(num, bin(num)))
elif opção == 2:
    print('{} Convertido em OCTAL é igual á {}'.format(num, oct(num)))
elif opção == 3:
    print('{} Convertido em HEXADECIMAL é igual á {}'.format(num, hex(num)))
else:
    print('Opção Inválida!')