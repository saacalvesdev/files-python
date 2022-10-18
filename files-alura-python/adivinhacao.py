import random

def jogar():
    print('****************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('****************************')

    num_secret = random.randrange(1,101)
    tot_de_tent = 3
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina seu nível: '))

    if(nivel == 1):
        tot_de_tent = 20
    elif(nivel == 2):
        tot_de_tent = 10
    elif(nivel == 3):
        tot_de_tent = 5

    for rodada in range(1, tot_de_tent + 1):
        print('Tentativa {} de {}'.format(rodada, tot_de_tent))
        chute_str = input('Digite um número entre 1 e 100: ')
        print('Você digitou', chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue 

        acertou = num_secret == chute
        maior = chute > num_secret
        menor = chute < num_secret

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Você Errou!, seu chute foi maior que o número secreto.')
            elif(menor):
                print('Você Errou!, seu chute foi menor que o número secreto.')
            pontos_perdidos = abs(num_secret - chute)
            pontos = pontos - pontos_perdidos
        print('Fim de Jogo!')

if(__name__== '__main__'):
    jogar()
 