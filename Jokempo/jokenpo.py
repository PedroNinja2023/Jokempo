import random

##PEDRA = 0, PAPEL = 1, TESOURA = 2
jogada_jogador = int(input("POSSÍVEIS JOGADAS \n PEDRA = 0; \n PAPEL = 1; \n TESOURA = 2. \n escolha a sua jogada:"))
jogada_cpu = random.randint(0,2)
match jogada_cpu:
    case 0:
        if jogada_jogador == 0:
            print("PEDRA X PEDRA \n EMPATE.")
        elif jogada_jogador == 1:
            print("PEDRA X PAPEL \n VITÓRIA DO JOGADOR.")
        elif jogada_jogador == 2:
            print("PEDRA X TESOURA \n DERROTA DO JOGADOR.")
    case 1:
        if jogada_jogador == 0:
            print("PAPEL X PEDRA \n DERROTA DO JOGADOR.")
        elif jogada_jogador == 1:
            print("PAPEL X PAPEL \n EMPATE.")
        elif jogada_jogador == 2:
            print("PAPEL X TESOURA \n VITÓRIA DO JOGADOR.")
    case 2:
        if jogada_jogador == 0:
            print("TESOURA X PEDRA \n VITÓRIA DO JOGADOR.")
        elif jogada_jogador == 1:
            print("TESOURA X PAPEL \n DERROTA DO JOGADOR.")
        elif jogada_jogador == 2:
            print("TESOURA X TESOURA \n EMPATE 1.")
print(jogada_cpu)