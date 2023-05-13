animales = ['gato','perro','leon','caballo']
nombres = ('julIo','mArio','camilo')
producto = {
  'name':'camisa',
  'brand':'Tommy',
  'price':25
}
people = [
  {'name':'luis',
  'age':25,
  'phone':'57+321456987'},
  {'name':'pedro',
  'age':32,
  'phone':'59+321456987'},
  {'name':'maria',
  'age':16,
  'phone':'3214'}
]

for number in range(1,21):
  print(number)

for animal in animales:
  index = animales.index(animal)
  animales[index] = animales[index].title()
  
print(animales) 
for nombre in nombres:
  print(nombre)

new_nombres = list(nombres)
for name in new_nombres:
  index = nombres.index(name)
  new_nombres[index] = new_nombres[index].upper()
print(new_nombres) 

for key, value in producto.items():
  if 'price' in key:
    producto['price'] = "$ "+str(value)
   
print(producto)

for person in people:
  person['name'] =  person['name'].title()
  if len(person['phone']) < 10:
    print('El número télefonico no corresponde con el parámetro')
    
print(people)    
  
  
  

 
  
  
  
  
  