while True:
    print('Olá! Qual é o seu nome?')
    nome = input()
    if nome != 'Victor':
        continue
    print('Digite sua senha!')
    senha = input()
    if senha == 'Gatinhos':
        break
    print('Senha incorreta')
print('Bem vindo, Victor!')