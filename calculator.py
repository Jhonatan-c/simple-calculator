def suma(num1, num2):
    print(num1 + num2)

def resta(num1, num2):
    print(num1 - num2)

def multi(num1, num2):
    print(num1 * num2)

def divi(num1, num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: División por cero")

print("----------------------------¡Bienvenido!----------------------------")
print("-----------------------------------------------------------------------------------------")
print("Esta es una calculadora sencilla, y para probarla puedes escoger los siguientes números: ")
print("-----------------------------------------------------------------------------------------")
print("[1] Suma \n[2] Resta \n[3] Multiplicación \n[4] División \n[5] Salir")

modo = int(input("===> "))

if modo == 5:
    print("¡Nos vemos pronto!")

try:
    num1 = int(input("Ingresa el primer valor de tu preferencia: "))
    num2 = int(input("Ingresa el segundo valor: "))
except ValueError:
    print("Error: Ingresa números válidos.")

if modo == 1:
    suma(num1, num2)
elif modo == 2:
    resta(num1, num2)
elif modo == multi:
    multi(num1, num2)
elif modo == 4:
    divi(num1, num2)

reiniciar = input("¿Deseas realizar otra operación? (s/n): ")
if reiniciar.lower() != "s":
    print("Hasta luego! Gracias por preferirnos.")