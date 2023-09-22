def filtra_pares(tupla):
    ''' recebe uma tupla com quatro elementos e retorna os elementos pares dessa tupla em uma outra tupla
    tuple->tuple'''
    pares= ()
    for i in tupla:
        if i%2 == 0:
            pares = pares + (i)
            
    return pares