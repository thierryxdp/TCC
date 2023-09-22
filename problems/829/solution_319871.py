def soma_h(n):
    h = 0
    for i in range(1, n +1 ):
        parcela = 1 / i
        h += parcela
    return round(h, 2)