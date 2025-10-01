import encript_function
import decription_function

direction = input("Ingresa 'encode' para encriptar o 'decode' para descencriptar \n")

while direction != "encode" and direction != "decode":
  direction = input("Ingresa 'encode' para encriptar o 'decode' para descencriptar \n")

text = input("Ingresa el mensaje que quieres encriptar: \n").lower()
shift = int(input("Ingresa el número de desplazamiento: \n"))

if direction == "encode":
  encript_function.encrypt(text, shift)
elif direction == "decode":
  decription_function.decrypt(text, shift)