import math

x = input('Insira um numero: ')
x = int(x)

sum = 0
for i in range(x+1):
    sum = sum + math.factorial(i)
    return sum