def filtra_pares(a):
    '''Dados quatro números de entradas, retorna somente os pares na ordem.'''
    pares = ()
    if (a[0]%2 ==0):
        pares = tuple(a[0])
    if (a[1]%2 == 0):
        pares = pares+tuple(a[1])
    if (a[2]%2 == 0):
        pares = pares +tuple(a[2])
    if(a[3]%2 == 0 ):
        pares = pares +tuple(a[3])
    return pares