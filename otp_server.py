import pyotp
import os

secret_key=pyotp.random_base32()
totp= pyotp.TOTP(secret_key)
while True:
    os.system("cls")
    print('''Menu de opciones:
    1. Mostrar clave secreta
    2. Verificar código
    3. Salir''')
    des=input("Ingrese su eleccion: ")
    if des=="1":
        print("La clave secreta es:",secret_key)
        os.system("pause")
    elif des=="2":
        psw=input("Ingrese el código: ")
        if totp.verify(psw):
            print("El código es válido :)")
        else:
            print("Este código no es válido o ya esta vencido :(")
        os.system("pause")
    elif des=="3":
        break
    else:
        print("Debe ingresar un numero entre 1-3")
        os.system("pause")