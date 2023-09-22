def filtra_pares(tupla):
    '''fucao que recebe uma tupla com quatro elementos, filtra apenas retorna os pares'''
    pares = ()
    if tupla [0]%2==0:
        pares = pares + (tup[0],)
        if tupla [1]%2==0:
            pares = pares + (tup [1],)
            if tupla [2]%2==0:
                pares = pares + (tup [2],)
                if tupla [3]%2==0:
                    pares = pares + (tup [3],)
                    return pares
                else:
                    return ()