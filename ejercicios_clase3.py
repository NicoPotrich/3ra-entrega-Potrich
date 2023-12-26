
print ('')
print ('ACTIVIDAD 1')
print ('')

nombres = input("Ingrese nombres separados por comas: ")
print ('')
nombres_unicos = set(nombres.split(','))
print ('Nombres unicos:', nombres_unicos)
print ('Cantidad de nombres unicos:', len(nombres_unicos))

######################################

print ('')
print ('Actividad 2')
print ('')

carrito = {
    'Manzana': 50,
    'Banana': 30,
    'Pera': 40
}

while True:
    producto = input('Ingrese el producto o Exit para salir: ')
    if producto == 'Exit':
        break
    else:
        cantidad = int(input('Ingrese la cantidad: '))
    carrito[producto] = cantidad

print (carrito)

######################################

print ('')
print ('Actividad 3')
print ('')

oracion = input('Ingrese una oracion: ')
print ('1) Oracion en mayusculas:', oracion.upper())
print ('2) Cuantas veces aparece Python: ', oracion.count('Python'))
print ('3) Oracion sin espacios en blanco:', oracion.strip())

######################################

print ('')
print ('Actividad 4')
print ('')

set1 = set(input('Ingrese numeros separados por comas para el set 1: ').split(','))
set2 = set(input('Ingrese numeros separados por comas para el set 2: ').split(','))

print ('')

set3 = set1.intersection(set2)
set4 = set1.union(set2)

print ('Numeros en comun:', set3)
print ('Union de ambos conjuntos:', set4)

######################################

print ('')
print ('Actividad COMPLEMENTARIA')
print ('')

person = {
    'nombre': '',
    'edad': '',
    'direccion': '',
}

for i in person:
    person[i] = input(f'Ingrese su {i}: ')

print (person)
