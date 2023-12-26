
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
print ('')
print ('Lista original:', lista)
print ('')

# 1)
lista_mod = set(lista)
print ('1) Borrar repetidos:', lista_mod)

# 2)
lista_mod = list(lista_mod)
lista_mod.sort()
lista_mod = lista_mod[::-1]
print ('2) Ordenar mayor a menor:', lista_mod)

# 3)
lista_mod = [num for num in lista_mod if num % 2 == 0]
print ('3) Eliminar numeros impares:', lista_mod)

# 4)
suma = sum(lista_mod)
print ('4) Suma de numeros en la lista:', suma)

# 5)
lista_mod.insert(0, suma)
print ('5) Añadir la suma como primer elemento:', lista_mod)

# 6)
print ('6) Devolver la lista modificada:', lista_mod)

# 7)
suma = sum(lista_mod[1:])
print ('7) Comprobar la suma:', suma)
print ('')
