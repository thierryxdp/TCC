def filtra_pares(a):
    '''Dados quatro números de entradas, retorna somente os pares na ordem.'''
    pares = ()
    if (a[0]%2 ==0):
        pares = (a[0],)
    if (a[1]%2 == 0):
        pares = pares+(a[1],)
    if (a[2]%2 == 0):
        pares = pares +(a[2],)
    if(a[3]%2 == 0 ):
        pares = pares +(a[3],)
    return pares