def filtra_pares(x):
    '''filtra os pares de uma tupla
    tupla -> tupla'''
    if x[2]%2==0 and x[3]%2==0:
        return x
    else:
        return x[:2]+x[3]
    if x[3]%2==0:
        return x
    else:
        return x[:3]