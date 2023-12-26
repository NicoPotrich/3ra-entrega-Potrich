# Desafio Tuplas
print ('ACTIVIDAD 1')
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print ('')
print ('1) ', tupla[-1])
print ('2) ', len(tupla))
print ('3) ', tupla.index(87))
print ('4) ', tupla[-3:])
print ('5) ', tupla[8])
print ('6) ', tupla.count(7))
print ('')

######################################

print ('ACTIVIDAD 2')
print ('')

frase = input('Escriba una frase: ')
primeros_tres = frase[0:3]
ultimos_tres = frase[-3:]

print ('')
print ('Primeros tres:', primeros_tres)
print ('Ultimos tres:', ultimos_tres)
print ('Concatenacion:', primeros_tres + ultimos_tres)
print ('')

######################################

print ('ACTIVIDAD 3')
print ('')

numeros = [2, 55, 84, 13, 45, 21, 65, 78, 32, 18]

print ('Lista:', numeros)
num = int(input('Ingrese un entero: '))
indice = int(input('Ingrese el indice (0 al 9): '))

if indice < len(numeros) -1:
    numeros[indice] = num
else:
    print ('El indice no existe')

print ('')
print ('Nueva Lista:', numeros)
print ('')

######################################

print ('ACTIVIDAD 4')
print ('')

palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")
print ('')
print ('palabras_tupla =', palabras_tupla)
print ('')
segundo_elemento = palabras_tupla[1]
print ('Valor del segundo elemento:', segundo_elemento)
print ('Se repite', palabras_tupla.count(segundo_elemento), 'veces')
print ('Indice del segundo elemento:', palabras_tupla.index(segundo_elemento, 2))
print ('')

######################################

print ('ACTIVIDAD COMPLEMENTARIA')
print ('')

matriz = [
    [1,5,1],
    [2,1,2],
    [3,0,1],
    [1,4,4]
]


matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print (matriz)

