def filtra_pares(x):
    '''retorna uma tupla apenas com os elementos pares da original
    (int,int,int,int) -> tupla com até 4 elementos'''
    if (x[0]%2)==0:
        return x[0],
    if (x[1]%2)==0:
        return x[1],
    if (x[2]%2)==0:
        return x[2],
    if (x[3]%2)==0:
        return x[3],
    else:
        return ()