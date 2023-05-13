name = "Gilbert"
age = 40
is_single = False
print(type(age))
print("Mi nombr es "+name+" y mi edad es "+str(age))

name = 51
age = False
is_single = "Luis"
print(type(age))

age = input("Ingresa tu edad: ")
print("Edad recibida por input: ",type(age))
age = int(age)
print("Edad casteada a int: ",type(age))

newAge = int(input("Ingresa tu edad: "))
print("Edad casteada direcytamente enel input: ",type(newAge))

