def filtra_pares(elementos_int):
    '''funcao que diz se os elementos da tupla sao pares; tupla -> tupla'''
    (elemento1,elemento2,elemento3,elemento4) = elementos_int
    par=()
    if elemento1[0] % 2 == 0:
        par=par+(elemento1[0],)
    if elemento2[1] % 2 == 0:
        par= par+(elemento2[1],)
    if elemento3[2] % 2 == 0:
        par=par+(elemento3[2],)
    if elemento4[3] % 2 == 0:
        par=par+(elemento4[3],)
    else:
        return par = ()
    par = ()