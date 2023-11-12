'''
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
[P[0,0]][P[0,1]][P[0,2]]
[P[1,0]][P[1,1]][P[1,2]]
[P[2,0]][P[2,1]][P[2,2]]

'''

print (25*'-=')
print('--------------------MATRIZ 3X3--------------------')
print (25*'-=')

l1 = [[],[],[]]
l2 = [[],[],[]]
l3 = [[],[],[]]
valor = 0
cont=0
continua=0
u=0


for p in range (0,3):
    if cont==0:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[0].append(valor)
       
        cont +=1
    if cont==1: 
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[1].append(valor)
        
        cont +=1
    else:
        valor= int (input(f'Digite uma valor para [0,{cont}]: '))
        l1[2].append(valor)
       
        cont +=1
    if cont >=3:
        break

for p in range (0,3):
    if continua==0:
        valor= int (input(f'Digite uma valor para [1,{continua}]: '))
        l2[0].append(valor)
        
        continua +=1
    if continua==1: 
        valor= int (input(f'Digite uma valor para [1,{continua}]: '))
        l2[1].append(valor)
       
        continua +=1
    else:
        valor= int (input(f'Digite uma valor para [1,{continua}]: '))
        l2[2].append(valor)
        
        continua +=1
    if continua >=3:
        break

for p in range (0,3):
    if u==0:
        valor= int (input(f'Digite uma valor para [2,{u}]: '))
        l3[0].append(valor)
        
        u +=1
    if u==1: 
        valor= int (input(f'Digite uma valor para [2,{u}]: '))
        l3[1].append(valor)
        
        u +=1
    else:
        valor= int (input(f'Digite uma valor para [2,{u}]: '))
        l3[2].append(valor)
        
        u +=1
    if u >=3:
        break

print(l1)
print(l2)
print(l3)

print ('\n',l1[0],l1[1],l1[2],'\n',l2[0],l2[1],l2[2],'\n',l3[0],l3[1],l3[2])
print('\n')
for i in l1:
    print(f' {i}',end='')
print()
for i in l2:
    print(f' {i}',end='')
print()
for i in l3:
    print(f' {i}',end='')
print('\n')


