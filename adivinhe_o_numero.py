print("============= ADIVINHE O NÚMERO =============")
print("\n")
print('   Tente adivinhar o número, você terá 5 chances')
print("\n")
print("         Primeiro, selecione a dificuldade do jogo:")
print("\n")
print("         1- FÁCIL: Adivinhe um número de 1 a 10")
print("         2- NORMAL: Adivinhe um número de 1 a 30")
print("         3- DIFÍCIL: Adivinhe um número de 1 a 50")


while True:
    dificuldade = int(input('\nDigite o nível de dificuldade: 1, 2 ou 3: '))
    if dificuldade <4 and dificuldade >0:
        break
    else: print("Digite novamente: 1, 2 ou 3:")
    
#DIFICULDADE 01
if dificuldade == 1:
    print("\n""Nivel: FÁCIL")
    escolha = int(input('\nEscolha um número de 1 a 10: '))
    import random 
    maquina = random.randint(1,10)

    tentativa = 5

    while tentativa > 0:
        if escolha == maquina:
            print("\n" "PARABÉNS, VOCE ACERTOU!!! O número era ", maquina)
            break
    
        elif escolha>maquina: print("\n" "o numero é menor")
        elif escolha<maquina: print("\n" "o numero é maior")
        print('\n')
        tentativa = tentativa -1
        if tentativa < 1 :
            print("VOCE PERDEU!! O número era ", maquina)
            break
        print("voce ainda tem ", tentativa , "chanches")
        escolha = int(input('\nEscolha um número de 1 a 10: '))

#DIFICULDADE 02
elif dificuldade == 2:
    print("\n""Nivel: NORMAL")
    escolha = int(input('\nEscolha um número de 1 a 30: '))
    import random 
    maquina = random.randint(1,30)

    tentativa = 5

    while tentativa > 0:
        if escolha == maquina:
            print("\n" "PARABÉNS, VOCE ACERTOU!!! O número era ", maquina)
            break
    
        elif escolha>maquina: print("\n" "o numero é menor")
        elif escolha<maquina: print("\n" "o numero é maior")
        print('\n')
        tentativa = tentativa -1
        if tentativa < 1 :
            print("VOCE PERDEU!! O número era ", maquina)
            break
        print("voce ainda tem ", tentativa , "chanches")
        escolha = int(input('\nEscolha um número de 1 a 50: ')) 
    
#DIFICULDADE 03    
elif dificuldade == 3:
    print("\n""Nivel: DIFICIL")
    escolha = int(input('\nEscolha um número de 1 a 50: '))
    import random 
    maquina = random.randint(1,50)

    tentativa = 5

    while tentativa > 0:
        if escolha == maquina:
            print("\n" "PARABÉNS, VOCE ACERTOU!!! O número era ", maquina)
            break
    
        elif escolha>maquina: print("\n" "o numero é menor")
        elif escolha<maquina: print("\n" "o numero é maior")
        print('\n')
        tentativa = tentativa -1
        if tentativa < 1 :
            print("VOCE PERDEU!! O número era ", maquina)
            break
        print("voce ainda tem ", tentativa , "chanches")
        escolha = int(input('\nEscolha um número de 1 a 10: '))