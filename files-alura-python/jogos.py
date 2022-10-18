import forca
import adivinhacao

def escolhe_jogo():
    print('****************************')
    print('Escolha o seu jogo!')
    print('****************************')

    print('(1) Adivinhação (2) Forca')
    jogo = int(input('Qual o seu jogo? '))

    if(jogo == 1):
        print('Jogando Adivinhação')
        adivinhacao.jogar()
        
    elif(jogo == 2):
        print('Forca')
        forca.jogar()

    if(__name__ == '__main__'):
        escolhe_jogo()