#Start your python function here
number = int(input('Digite um número: '))
if(number%2==0):
 list_numbers = list(range(0, number + 1, 2))
 print(list_numbers)