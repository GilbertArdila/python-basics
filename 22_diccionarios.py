diccionario = {
  'avion':'plane',
  'casa':'house',
  'carro':'car'
}

person = {
  'name':'Andres',
  'lastName':'Lopez',
  'age':25,
  'phone':'57+3215558899',
  'languages':['Spanish','English']
}
print(type(diccionario))
print(len(person))
print(diccionario['casa'])
print(person.get('lastName'))
print(person.get('lastNamessss'))
print('avion' in diccionario)
print('lalaal' in diccionario)
print(person)
person['name'] = 'Andrea'
person['age'] -= 2
person['languages'].append('Italian')
print(person)
del person['phone']
person.pop('lastName')

print(person.items())
print(person.keys())
print(person.values())

