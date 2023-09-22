def soma_h(n):
    '''retorna o valor de h dado n numeros
    int -> float'''
    h = 1

    for i in range(2, n+1):

        h += (1/i)
    return float (round (h,2))