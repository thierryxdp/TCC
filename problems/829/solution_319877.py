# Soma de H

def soma_h(n):
    '''Dado um número n, retorna o valor de h, sendo h = 1 + 1/2 + ... + 1/n
    int -> float'''
    soma = 0
    for x in range(n):
        soma += 1/(x+1)
    return round(soma,2)