#Tuplas, inmutables
numbers = (1,2,3,4,5,6,0,25,9,3)
strings = ('Maria','Luis')

print(type(strings))
print(numbers[5])
index = numbers.index(25)

print(numbers.count(3))
print(index)

#transformaciones
new_numbers = list(numbers)

print(type(new_numbers))
numbers3 = tuple(new_numbers)
print(type(numbers3))