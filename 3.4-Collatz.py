import sys

print('Digite um número')

try:
    numero = int(input())
except ValueError:
    print('Valor não é um número inteiro')
    sys.exit()

def CollatzSequence(numero):
    if numero % 2 == 0:
        print(numero // 2)
        return numero // 2
    else:
        print(3 * numero + 1)
        return 3 * numero + 1

while numero != 1:
    numero = CollatzSequence(numero)