name = "Gilbert"
lastName = "Ardila"
age = 40
height = 1.76

#format
concat = "hola mi nombre es "+name+" "+lastName+" mi edad es "+str(age)+" años y mi estatura es "+str(height)+" mts"
print(concat)

data = f"hola mi nombre es {name} {lastName} y mi edad es {age} años, mi altura es {height} mts"
print(data)

template = "hola mi nombre es {} {} y mi edad es {} años, mi altura es {} mts".format(name,lastName,age,height)
print("template: ",template)