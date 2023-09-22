filtra_pares(x,y,z,w):
    '''Dados quatro números de entradas, retorna somente os pares na ordem.'''
    pares = ()
    if (x%2 ==0):
        pares = pares+(x)
    if (y%2 == 0):
        pares = pares+(y)
    if (z%2 == 0):
        pares = pares +(z)
    if(w%2 == 0 ):
        pares = pares +(w)
    return pares