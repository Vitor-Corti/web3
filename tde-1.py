#1Peça ao usuário um número inteiro e calcule o dobro desse número.


x= int(input('Digite um valor para descobrir o seu dobro'))
x2= x*2


print(f'O dobro de {x} é {x2}')




#2Solicite a largura e a altura de um retângulo e calcule a área.


larg = float(input('Digite a largura do retangulo'))


alt = float(input('Digite a altura'))


print(f'A área do retangulo é{alt * larg:.2f}')


#3. Peça dois números inteiros e use o operador de igualdade (==) para verificar se eles são iguais.




x= int(input('digite um valor'))
x2= int(input('Digite outro valor para verificar se ele é igual ao outro'))


print(x == x2)




#3Peça dois números inteiros e calcule o resto da divisão entre eles usando o operador
#módulo (%).


x= int(input('digite um valor'))
x2= int(input('digite outro valor'))


print(f' o reesto da sua divisão: {x % x2}')


#5. Solicite três números e calcule a média aritmética simples deles.


x= int(input('digite um valor'))
x2= int(input('digite outro valor'))
x3= int(input('digite outro valor'))


media= (x+x2+x3)/3


print(f'a média{media:.2f}')


'''
#4Peça dois números e verifique se o primeiro é maior que 10 e o segundo é menor que 5
#usando o operador and.


x= int(input('digite um valor'))
x2= int(input('digite outro valor'))


print(x> 10 and x2<5)
