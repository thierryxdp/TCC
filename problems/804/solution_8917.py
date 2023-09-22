def filtra_pares(t):
    '''função que receba uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla origina '''
    pares = ()
    if t[0]%2 == 0:
        pares = pares + (t[0],)
    if t[1]%2 == 0:
        pares = pares + (t[1],)
    if t[2]%2 == 0:
        pares = pares + (t[2],)
    if t[3]%2 == 0:
        pares = pares + (t[3],)
    return pares