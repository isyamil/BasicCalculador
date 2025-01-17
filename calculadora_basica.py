
a = int(input('Introduce el primer numero: '))
b = int(input('Introduce el segundo numero: '))

operadores = {
    '1' : lambda a,b: a+b,
    '2' : lambda a,b: a-b,
    '3' : lambda a,b: a*b,
    '4' : lambda a,b: a/b if b != 0 else 'Estas diviendo por 0'
}

print(''' 
Que operación quieres hacer:

1)Sumar
2)Restar
3)Multiplicar
4)Dividir
5)Salir
''')

operador = (input('--> '))



resultado = operadores[operador](a,b)
print(f'El resultado es {resultado}')