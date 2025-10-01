import encript_function
import decription_function

direction = input("Ingresa 'encode' para encriptar o 'decode' para descencriptar \n")

while direction != "encode" and direction != "decode":
  direction = input("Ingresa 'encode' para encriptar o 'decode' para descencriptar \n")

text = input("Ingresa el mensaje que quieres encriptar: \n").lower()
shift = int(input("Ingresa el número de desplazamiento: \n"))

def decrypt(text, shift):
  new_text = ""
  for i in text:
    if i in alphabet:
      position = alphabet.index(i)
      if position - shift < 0:
        new_position = position - shift + 26
      else:
        new_position = position - shift
      new_letter = alphabet[new_position]
      new_text += new_letter
    else:
      new_text += i
  print(new_text)

if direction == "encode":
  encript_function.encrypt(text, shift)
elif direction == "decode":
  decription_function.decrypt(text, shift)