text = 'Ella sabe python'
print('Java' in text)
if 'python' in text:
  print("Sí está")
else:
  print("No está")

size = len(text)
print(size)
print(text.upper())
print(text.lower())
print(text.isupper())
print(text.islower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('java'))
print(text.replace('python','Go'))
print(text.capitalize())
print(text.title())
print('395'.isdigit())
print('hola'.isalpha())
print('hola123'.isalnum())