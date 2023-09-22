filtra_pares(x,y,z,w):
    '''retorna uma nova tupla contendo apenas os elementos pares da tupla original'''
    pares=()
    for n in (x,y,z,w):
        if n%2==0:
            pares.append(n)
    return pares