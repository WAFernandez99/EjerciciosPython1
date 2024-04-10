#print('Hello World')
#RL= float(input('Ingrese rendimiento del litro x m2'))
#M= int(input('Ingrese la cantidad de manos que desea dar'))
#L= float(input('Ingrese el largo en metros'))
#An= float(input('Ingrese el Ancho en metros'))
#A= float(input('Ingrese el Alto en metros'))
#Area= ((L * A)* 2) + ((An * A)* 2)
#T= L * An
#BT= Area + T
#BTM= BT * M
#Res= BTM / RL
#print('Usted necesita', Res ,'litros')


#Actividad 1 de operaciones basicas
#A= 186
#B= 24
#Suma= A + B
#Resta= A - B
#Multi= A * B
#Div= A / B
#Dive= A // B
#Resto= A % B
#Lista= Suma, Resta,Multi, Div,Dive, Resto
#print('El resultado de suma,resto, multi, div, dive, resto se mostrara respesctivamente en ese orden.', Lista)

#Actividad 2 
#A= 16823
#UD= A % 10
#DD= A % 100
#TD= A % 1000
#CD= A// 10
#PD= A // 10000
#PDD= A // 1000
#Lista= ('a',UD, 'B',DD, 'C', TD, 'D',CD, 'E',PD, 'F',PDD,)
#print('Resultado',Lista)

#Actividad 3
#Dadas las variables str1 = “Juan” y str2 = “Pérez”, ¿cómo harías para mostrar...
str1= 'Juan' 
str2= 'Pérez '
#a) Las dos cadenas concatenadas, mostrando apellido y nombre? Ejemplo: “Pérez Juan”
name= str2 + str1
print('El nombre es', name)
#b) Las dos cadenas concatenadas pero separadas por “, “? Ejemplo: “Pérez, Juan”
print('El nombre es',str2,',',str1,)
#c) nombre y apellidod) “¡Bienvenido, Juan Pérez!”

str3= 'Bienvenido'
bn= str3 + str1 + str2
print(bn)

#Activida 4
cadena1 = '¡Bienvenidos!'
cadena2 =  'esto es '
cadena3 =  'Introducción a la Informática'
cadena4 =  ' lo más divertido'
cadena5 =  'de primer año '
cadena6 =  ' ...(ponele)' 
#a) Construir la cadena “Bienvenidos esto es de primer año lo más divertido...(ponele) Introduccióna la Informática”.
cc= cadena1.strip('!')+ cadena2+ cadena5+ cadena4 + cadena6 +cadena3
print(cc)
#b) ¿En qué posición de la cadena anterior está la palabra “primer”?
pc= cc.find('primer')
print(pc)
#c) Buscar la primera posición en que aparece la letra “e” en cadena1.
pe= cadena1.find('e')
print(pe)
#d) Si buscás la letra “n” en cadena1, ¿qué resultado dará? 4 ¿Por qué? Porque toma el primer valor.
pn= cadena1.find('n')
print(pn)
#e) Obtener True o False para saber si cadena6 contiene espacios.
if (cadena6.count(' ')>0):
     print(True)
else:
     print(False)

#f) ¿Qué resultado se obtiene al buscar la letra “d” en cadena4[:6]? ¿Por qué?
rd= cadena4[:6].find('d')
print('Devuelve la posición de la letra "d" dentro de los primeros 6 caracteres de la cadena4')

#g) ¿Cuántos espacios tiene la cadena construida en el punto a?
ec= cc.count(' ')
print('Cantidad de espacios en la cadena', ec)

#Actividad 5
#Si tenemos la cadena texto = ‘No sé bien qué día es hoy’, indicá cómo obtener:
cadenatexto= 'No sé bien qué día es hoy'

#a) La cadena ‘qué día’ a partir de la variable texto.
vta= cadenatexto[10:17]
print()
#b) Los primeros 5 caracteres de texto.
vt5= cadenatexto[:5]
print()
#c) Los últimos 5 caracteres de texto.
vu5= cadenatexto[-5:]
print()
#d) Los caracteres ubicados en las posiciones pares de texto.


#e) La cadena ‘ye né’ a partir de texto.


#f) Cuántas ocurrencias de la letra ‘e’ existen en texto (incluir la ‘e’ con y sin acentos)



