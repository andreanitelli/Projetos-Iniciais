print("                              ***CALCULO DE FATORIAL***")
print('\n')

while True:
    numero = input('\nDigite um numero inteiro:')
    try:
        numero = int(numero)
        break
    except ValueError:
        print("\n", "(", numero, ")", "não é número inteiro")

fatorial = numero-1
total = fatorial*numero

while fatorial > 1:
    fatorial = fatorial-1
    total = total*fatorial

print('\n')
print("                              O fatorial de", numero, "é", total)
