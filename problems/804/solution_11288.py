def filtra_pares((el1,el2,el3,el4)):
    '''retorna uma tupla apenas com os elementos pares da original
    (int,int,int,int) -> tupla com até 4 elementos'''
    if (el1%2)==0:
        return el1,
    if (el2%2)==0:
        return el2,
    if (el3%2)==0:
        return el3,
    if (el4%2)==0:
        return el4,
    else:
        return ()