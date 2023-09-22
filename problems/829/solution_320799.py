import math as m
def soma_h(n):
    soma = 0
    for x in range(1,n+1):
        soma = 1/x + soma
    soma = round(soma, 2)
    return soma