
# Desafio Numeros

print ('')
print ('Desafio Numeros')
print ('-'*15)

partidos_ganados = int(input('Ingrese cantidad de partidos ganados: '))
partidos_empatados = int(input('Ingrese cantidad de partidos empatados: '))
partidos_perdidos = int(input('Ingrese cantidad de partidos perdidos: '))

total_partidos = partidos_ganados + partidos_empatados + partidos_perdidos

total_puntaje = partidos_ganados * 3 + partidos_empatados

promedio = total_puntaje / total_partidos
print ('')
print ('El promedio de puntos es =>', promedio)


# Desafio Strings

print ('')
print ('Desafio Strings')
print ('-'*15)

cadena_1 = 'versatil'
cadena_2 = 'Python'
cadena_3 = 'es un lenguaje'
cadena_4 = 'de programacion'

objetivo = cadena_2 + ' ' + cadena_3 + ' ' + cadena_4 + ' ' + cadena_1

print ('Frase concatenada =>', objetivo)


# Desafio Slicing

print ('')
print ('Desafio Slicing')
print ('-'*15)

cadena = 'acitametaM ,5.8 ,otipeP ordeP'
cadena_volteada = cadena[::-1]

nombre_alumno = cadena_volteada.split(',')[0]
nota = cadena_volteada.split(',')[1]
materia = cadena_volteada.split(',')[2]

print (f'{nombre_alumno} ha sacado un {nota} en {materia}')


# Actividad extra

print ('')
print ('Actividad extra')
print ('-'*15)

nota_1 = float(input('Nota 1: '))
nota_1 *= .2
nota_2 = float(input('Nota 2: '))
nota_2 *= .3
nota_3 = float(input('Nota 3: '))
nota_3 *= .5

suma_total = nota_1 + nota_2 + nota_3
print ('')
print ('Nota final =>', suma_total)
