#Fatorial
def fatorial(num):
    #dado um número, calcule o fatorial deste número; Int => int#
    i = 1
    for num in range(2, num + 1):
        i = i * num
    return(i)