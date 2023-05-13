#float
x = 3.3
y = 1.1 + 2.2
print(x == y)
#pasarlo a string
y_string = format(y,".2g")
print(str(x) == y_string)
#forma matemática
tolerance = 0.00001
print(abs(x-y) < tolerance)