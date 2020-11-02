# Parte de scrypt.py
# Documentacion de: https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html
# Integrantes:
# Jorge Azmitia
# Cristina Bautista
# Sebastian Maldonado
# Abril Palencia
# Cesar Rodas

from passlib.hash import scrypt

def opcion1(password):
  h = scrypt.using(salt=b'salt', salt_size=1024, rounds=8, block_size=8,
    parallelism=1, relaxed=True).hash(password)
  return h

def opcion2(password, h):
  verify = scrypt.verify(password, h)
  if verify == True:
    return print("Nitido, es la misma password")
  else:
    return print("No es la misma password, vuelve a intentarlo")

a = 0
while a != 3:
  print("""
  1. Ingresar password
  2. Comparar password
  3. Salir
  """)
  a = int(input("Escoja una opcion: "))
  if a == 1:
    password = input("Ingrese una password: ")
    hpassword = opcion1(password)
  elif a == 2:
    password2 = input("Ingrese una password para comparar con la password de la opcion 1: ")
    opcion2(password2, hpassword)
  elif a == 3:
    print("Hasta la proxima, amigos")
    a = 3