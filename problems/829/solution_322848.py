def soma_h(n):
    '''H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
    Dado o número inteiro N, retorna o valor H conforme
    a fórmula acima.
    int -> float'''
    h = 0
    for i in range(1,n+1):
        h += 1/i
    return round(h,2)