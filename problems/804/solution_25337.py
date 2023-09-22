def par(x):
    '''retorna True se x é par e False se não é; float --> bool'''
    return x%2 == 0
        
def filtra_pares(t):
    '''retorna tupla com os números pares da tupla t que possui 4 elementos; tuple(float,float,float,float) --> tuple'''
     pares = ()

    if par(t[0]):
        pares = pares + (t[0])
    if par(t[0]):
        pares = pares + (t[1])
    if par(t[0]):
        pares = pares + (t[2])
    if par(t[0]):
        pares = pares + (t[3])
    return pares