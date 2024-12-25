print("============= RESOLVENDO EQUAÇÃO DE 2º GRAU : BHASKARA =============")
print("\n")
print('   (a).x² + (b).x + c = 0')
print("\n")
print("         ∆ = b² - 4.a.c")
print("         x = (-b ± √∆)/(2.a)")



while True:
    a = input('\nDigite o valor de "a":')
    try:
        a = float(a)
        break
    except ValueError:
        print("\n", "(" , a, ")", "não é número")
        
    
while True:
    b = input('\nDigite o valor de "b":')
    try:
        b = float(b)
        break
    except ValueError:
        print("\n", "(" , b, ")", "não é número")
        
while True:
    c = input('\nDigite o valor de "c":')
    try:
        c = float(c)
        break
    except ValueError:
        print("\n", "(" , c, ")", "não é número")

print('\n')

delta = float(b*b - 4*a*c)

if delta<0:
    print("\nO valor de ∆ não pode ser calculado: Valor negativo")
else:

    rdelta = delta**0.5

    x1a=(-b+rdelta)
    x1b=2*a
    x1=x1a/x1b

    x2a=(-b-rdelta)
    x2b=2*a
    x2=x2a/x2b

    print("As raizes da equação são:", round(x1,2), "e", round(x2,2))