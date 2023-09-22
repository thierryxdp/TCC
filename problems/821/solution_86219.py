def factorial():
num = int(input('1'))
fat = 1
while num != 0:
    fat *= num
    num -= 1
print(fat)