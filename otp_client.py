import pyotp
import os

generado=False
while True:
    os.system("cls")
    print('''Menu de opciones:
    1. Ingresar clave secreta
    2. Generar código
    3. Salir''')
    des=input("Ingrese su eleccion: ")
    if des=="1":
        secret_key=input("Ingrese la clave secreta: ")
        totp=pyotp.TOTP(secret_key)
        generado=True
    elif des=="2":
        if generado:
            print("El código es:",totp.now())
        else:
            print("Por favor ingrese la clave secreta primero")
        os.system("pause")
    elif des=="3":
        break
    else:
        print("Debe ingresar un numero entre 1-3")
        os.system("pause")
