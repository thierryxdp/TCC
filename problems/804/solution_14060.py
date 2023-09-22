def filtra_pares(elementos_int):
    '''funcao que diz se os elementos da tupla sao pares; tupla -> tupla'''
    (elemento1,elemento2,elemento3,elemento4) = elementos_int
    par=()
    if elemento1 % 2 == 0:
        return par=par+(elemento1,)
    elif elemento2 % 2 == 0:
        return par= par+(elemento2,)
    elif elemento3 % 2 == 0:
        return par=par+(elemento3,)
    elif elemento4 % 2 == 0:
        return par=par+(elemento4,)
    else:
        return par = ()
    par = ()