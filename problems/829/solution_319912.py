def soma_h(n):
    '''Dado um número inteiro 'n', calcula 'h', sendo:
     h = 1 + 1/2 + 1/3 + 1/4 ... + 1/n

     int -> float'''

    h = 0

    for elemento in range(1, n+1):
        h = h + 1/elemento

    return round(h, 2)