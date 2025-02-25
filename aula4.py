# tuplas- conjunto de dados,é imutavel, é representado pelo()
'''
a= (1,2,3,4,5,'Vitor',True)

print(a)
print(a[4])
print(a[-3])
print(a[1:4])
print(a[3:])
print(a[:3])# o final é a posição -1


# concatenização de tupla - + ----------------------------------------

b = (1,2,3,4,5)
c= (6,7,8,9,10)
#d= b +c
#print(d)
print( b + c)

#len() mostra a quantidade e elementos de uma tupla ou lista---------------

nome = ('Thereza', 'Julia', 'Paulo', 'Marcelin')
t= len(nome)
print(f'A quantidade de elementos da tupla é {t}')
print(f'A quantidade de elementos da tupla é {len(nome)}')

#--------------------------------------------------------------------

for i in range(0, len(nome)):
    print(f'olá {nome[i]}. Bom dia')

for i in range(len(nome)):
    print(f'olá {nome[i]}. Bom dia')


#del()- deletar tupla inteira -----------------
e= (1,2,3,4,5)

print(e)

del(e)
print(e)


e= (1,2,3,4,5)
del(e[1][3])
print(e) #resposta erro, a tupla n pode ser alterada, n se pode apagar elementos dela, ou apaga ela toda ou n apaga

# count() - mostra a quantidade de vezes que um determinado elemento repete---------------

f= (1,4,5,2,3,4,8,9,4)
print(f'O número 4 repete { f.count(4)} vezes')
print(f'O número 1 repete { f.count(1)} vezes')

#index() - mostra a posição de um determinado elemento e quando houver repetição ele mostra primeira posição
# do valor repetido -------

print(f'O indice da primeira posição é {f.index(4)}')
print(f'O indice da primeira posição é {f.index(9)}')


#lista() - conjunto de dados, mutavel, sua representação é[]-------

a= [1,2,3,4,5,'Vitor',True]
print(a)
print(a[4])
print(a[-3])
print(a[1:4])
print(a[3:])
print(a[:3])

a[-2] = 'abacate'
print(a)



i= [1,[1,3,3],4,5,6,[7,8,9], False]
print(i)
print(i[5][0])
print(i[1][-1])

#concatenar lista ----------------------------------

b= [1,2,3,4,5]
c=[6,7,8,9,10]
print(b+c)

#append() - inserir novos elementos no FINAL da lista-------------------------

b.append('Marcelin')
print(b)

b.extend('Marcelin')
print(b)

#recebendo valores externos---------------------------------

aluno =[] # ou list()

nome1= input(f'digite  o nome do aluno: ')
nome2= input(f'digite  o nome do aluno: ')
nome3= input(f'digite  o nome do aluno: ')
nome4= input(f'digite  o nome do aluno: ')
aluno.append(nome1)
aluno.append(nome2)
aluno.append(nome3)
aluno.append(nome4)
print(aluno)

#-----------------------------------------------------------------------------
numero = list()

for i in range(10,30,2):
    numero.append(i)
print(numero)


#insert() inserir novos elementos na  lista ESCOLHENDO A POSIÇÃO DESEJADA---------------------------

k= [1,2,3,4,5]
print(k)
k.insert(3, 'A')
print(k)

#remove- remover um determinado elemento na lista ------------------------

k.remove('A')
print(k)


#max() - mostra o maior valor da lista ----------------------------

m= [100,20,30,40,1,1]

print(f'O maior valor da lista é {max(m)}')

#min() - mostra o menor valor da lista ----------------------------

m= [100,20,30,40,1,1]

print(f'O maior valor da lista é {min(m)}')



notas =[0] * 3
for i in range(3):
    notas[i] = float(input(f'digite a nota: '))
media = ((notas [0] + notas[1] + notas[2]) / 3)
print(f'A media do aluno é {media:.1f}')

# reverse() - inverter a lista-----------------

n = [1,5,4,8,0,3,4]
print(n)
n.reverse()
print(f'a lista invertida é {n}')

#-------------------------------------------------------------

d=[]
for i in range (5):
    num= float( input(f'Digite um número: '))
    d.append(num)
    d.reverse()
print(f'A lista invertida é {d}')
#sum - soma todos os valores da lista--------------------

print(f'a soma dos valores da lista é {sum(d)}')



#pop() apaga o ultimo elemento da lista----------------

x=[1,2,3,4,5]
#x.pop()
#print(x)

x.pop(2)
print(x)

#del() - apagar o ultimo elemento da lista, podendo ainda definir o intervalo

del(x[1:3])
print(x)


#sort() - para ordenar a lista em ordem crescente

l=['b','l','c','a']
l.sort()
print(l)

l.sort(reverse=True)#ordem decrescente
print(l)

'''

lista=[10,20,30,40,50]
for i, v in enumerate(lista):
    print(f'Indice = {i} Valor = {v}')