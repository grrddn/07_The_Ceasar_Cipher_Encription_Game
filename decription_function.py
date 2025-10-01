alphabet = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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