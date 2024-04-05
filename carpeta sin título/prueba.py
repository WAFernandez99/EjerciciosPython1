print('Hello World')
RL= float(input('Ingrese rendimiento del litro x m2'))
M= int(input('Ingrese la cantidad de manos que desea dar'))
L= float(input('Ingrese el largo en metros'))
An= float(input('Ingrese el Ancho en metros'))
A= float(input('Ingrese el Alto en metros'))
Area= ((L * A)* 2) + ((An * A)* 2)
T= L * An
BT= Area + T
BTM= BT * M
Res= BTM / RL
print('Usted necesita', Res ,'litros')


