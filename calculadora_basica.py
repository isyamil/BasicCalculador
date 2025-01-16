
a = int(input('Introduce el primer numero: '))
b = int(input('Introduce el segundo numero: '))
c = 0


print(''' 
Que operación quieres hacer:

1)Sumar
2)Restar
3)Multiplicar
4)Dividir
5)Salir
''')

operacion = int(input('-->'))

if operacion ==1:
    c = a + b
    print(f'El resultado de {a} + {b} es {c}')
if operacion ==2:
    c = a + b
    print(f'El resultado de {a} - {b} es {c}')
if operacion ==3:
    c = a + b
    print(f'El resultado de {a} * {b} es {c}')
if operacion ==4:
    c = a + b
    print(f'El resultado de {a} / {b} es {c}')
if operacion ==5:
    print('QUE')