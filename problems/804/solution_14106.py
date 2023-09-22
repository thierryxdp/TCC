def filtra_pares(elementos_int):
    '''funcao que diz se os elementos da tupla sao pares; tupla -> tupla'''
    (elemento1,elemento2,elemento3,elemento4) = elementos_int
    par = ()
    if elemento1 % 2 == 0:
        par = par+(elemento1,)
    if elemento2 % 2 == 0:
        par = par+(elemento2,)
    if elemento3 % 2 == 0:
        par = par+(elemento3,)
    if elemento4 % 2 == 0:
        par = par+(elemento4,)
    return par