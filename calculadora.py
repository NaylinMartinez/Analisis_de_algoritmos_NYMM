import math
import time

while True:

    def Suma ():
        resultado = num1 + num2 
        print("El resultado de la suma es:",resultado)

    def Resta ():
        resultado = num1 - num2 
        print("El resultado de la resta es:",resultado)

    def Multiplicacion ():
        resultado = num1 * num2 
        print("El resultado de la multiplicacion es:",resultado)

    def Division ():
        resultado = num1 / num2 
        print("El resuktado de la division es:",resultado)

print("______________________")
print("******MENÚ******")
print("______________________")
print("1). SUMA")
print("______________________")
print("2). RESTA")
print("______________________")
print("3). MULTIPLICACION")
print("______________________")
print("4). DIVISION")
print("______________________")
print("5). SALIR")
print("______________________")

entrada = int(input("¿QUÉ OPERACIÓN DESEA REALIZAR?"))

if entrada == 1:

    print("Opción 1). SUMA")
    num1 = int(input("Ingrese el primer número:"))
    num1 = int(input("Ingrese el segundo número:"))
    Suma ()
    time.sleep(2)


if entrada == 2:

    print("Opción 2). RESTA")
    num1 = int(input("Ingrese el primer número:"))
    num1 = int(input("Ingrese el segundo número:"))
    Resta ()
    time.sleep(2)

    
if entrada == 3:

    print("Opción 3). MULTIPLICACIÓN")
    num1 = int(input("Ingrese el primer número:"))
    num1 = int(input("Ingrese el segundo número:"))
    Multiplicacion ()
    time.sleep(2)

if entrada case== 4
    print("Opción 4). DIVISIÓN")
    num1 = int(input("Ingrese el primer número:"))
    num1 = int(input("Ingrese el segundo número:"))
    Division ()
    time.sleep(2)

if entrada == 5:
    print("Opción 5). salir")
    print("GRACIAS.")