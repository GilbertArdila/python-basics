
counter = 0
options = ('Piedra','papel','tijera')


option = input('ingresa una opción: ')
while option not in options:
  print('Opción incorecta, intenta de nuevo')
  option = input('ingresa una opción: ')
  counter+=1
  if counter == 3:
    print("demasiados intentos...")
    break 

counter2 = 0
while counter2 < 20:
  
  counter2+=1
  if counter2 < 15:
    continue
  print(counter2)  
    
  
  