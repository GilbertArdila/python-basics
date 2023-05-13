numbers = []
names = ['Carolina']
#Create
numbers.append('Luisa')
numbers.append('Carlos')
numbers.insert(1,'Andrea')
print(numbers)
#Update
numbers[0]='Lisa'

#Read
print(numbers)
new_list = names + numbers
index = new_list.index('Carlos')
new_list[index] = 'Carlitos'
print(new_list)

#Delete
numbers.remove('Lisa')
numbers.pop()
new_list.pop(1)

new_list.reverse()
print(new_list)

numbers2 = [1,15,3,8,12,9]
text = ['re','al','zu','pt']
numbers2.sort()
print(numbers2)
text.sort()
print(text)
