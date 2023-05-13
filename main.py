import random
options = ('piedra','papel','tijera')
rounds = 1
computer_score = 0
user_score = 0
ties = 0
counter = 0

while rounds <= 3:
  print('*'*50)
  print('Round ',rounds,'Computer: ',computer_score,' User: ',user_score,' Ties: ',ties)
  print('*'*50)
  user_option = input("elige piedra, papel o tijera: ")
  user_option = user_option.lower()
  rounds += 1  
  if not user_option in options:
      print('Opción incorecta, intenta de nuevo')
      counter+=1
      if counter == 3:
        print("demasiados intentos...")
        print('Intentalo luego!')
        break
  if  user_option in options:
    computer_option =  random.choice(options)
    print('Tu opción: ', user_option)
    print('Mi elección: ', computer_option)
    if user_option == computer_option:    
      print("Empate")
      ties += 1
    elif user_option == "papel":
      if computer_option == "piedra":
        print("ganaste")
        user_score+=1
      else:
        print("perdiste")
        computer_score+=1
    elif user_option == "tijera":
      if computer_option == "piedra":
        print("perdiste")
        computer_score+=1
      else:
        print("ganaste") 
        user_score+=1
    elif user_option == "piedra":
      if computer_option == "papel":
        print("perdiste")
        computer_score+=1
      else:
        print("ganaste")
        user_score+=1
    if computer_score == 2:
      print('Computer has 2 wins, you lose!')
      break
    elif user_score == 2:
      print('You have 2 wins, you win!')
      break
           
print('*'*50)
print(' '*10,'********Total Score********')
print('Computer: ',computer_score,' User: ',user_score,' Ties: ',ties)
print('*'*50)        
  
'''
if not user_option in options:
  print('Opción invalida')
else:  
  computer_option =  random.choice(options)

  print('Tu opción: ', user_option)
  print('Mi elección: ', computer_option)

  if user_option == computer_option:
    print("Empate")
  elif user_option == "papel":
    if computer_option == "piedra":
      print("ganaste")
    else:
      print("perdiste")
  elif user_option == "tijera":
    if computer_option == "piedra":
      print("perdiste")
    else:
      print("ganaste") 
  elif user_option == "piedra":
    if computer_option == "papel":
      print("perdiste")
    else:
      print("ganaste")     
      '''
  
  