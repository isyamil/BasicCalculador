operacion = input('Dime que operación quieres hacer:\n1)Suma\n2)Resta\n3)Multiplicación\n4)División\n---> ')
operacion = int(operacion)
number1 = int(input('Dime el primero número: '))
number2 = int(input('Dime el segundo número: '))

if operacion == 1:
    print(f'Tu resultado es: {number1 + number2}')
elif operacion == 2:
    print(f'Tu resultado es: {number1 - number2}')
elif operacion == 3:
    print(f'Tu resultado es: {number1 * number2}')
elif operacion == 4:
    print(f'Tu resultado es: {number1 / number2}')
else:
    print('Hubo un error')