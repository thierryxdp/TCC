import math
def qtd_divisores(n):
    '''retorna o números de divisores do inteiro n'''
    qtd=2
    for i in range(1,math.floor(n/2):
        if n%i==0:
            qtd+=1
    return qtd