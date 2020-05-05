# Este é um jogo de adivinhar o número.
import random
numeroSecreto = random.randint(1, 20)
print('Estou pensando em um número entre 1 e 20.')
# Pergunta pelo número seis vezes.
for tentativasFeitas in range(1, 7):
    print('Faça uma tentativa.')
    tentativa = int(input())
    if tentativa < numeroSecreto:
        print('Seu número é muito baixo.')
    elif tentativa > numeroSecreto:
        print('Seu número é muito alto.')
    else:
        break # Tentativa correta!
if tentativa == numeroSecreto:
    print('Parabéns! Você acertou meu número em ' + str(tentativasFeitas) + ' tentativas!')
else:
    print('Poxa! O número que eu pensei era ' + str(numeroSecreto))