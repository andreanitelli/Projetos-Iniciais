print("***CALCULADORA EM PYTHON***")
print('\n')
print('Selecione o numero desejado:')
print('\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')

operação = input('Digite sua opção (1, 2, 3 ou 4):')
print('\n')

if operação == '1': 
    print('SOMA')
    s1 = float(input('digite o primeiro valor: '))     
    s2 = float(input('digite o segundo valor: '))
    st = s1+s2
    print(s1,'+', s2, '=' , st)

elif operação == '2':
    print('SUBTRAÇÃO')
    sb1 = float(input('digite o primeiro valor: '))     
    sb2 = float(input('digite o segundo valor: '))    
    sbt = sb1-sb2
    print(sb1,'-', sb2, '=' , sbt)
    
elif operação == '3': 
    print('DIVISÃO')
    d1 = float(input('digite o primeiro valor: '))    
    d2 = float(input('digite o segundo valor: '))    
    dt = d1/d2
    print(d1,'/', d2, '=' , dt)
    
elif operação == '4':  
    print('MULTIPLICAÇÃO')
    m1 = float(input('digite o primeiro valor: '))    
    m2 = float(input('digite o segundo valor: '))    
    mt = m1*m2
    print(m1,'x', m2, '=' , mt)
    
else: print('operação inválida')

