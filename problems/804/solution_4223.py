def filtra_pares(x):
    '''filtra os pares de uma tupla
    tupla -> tupla'''
    if x[0]%2==0:
        return x
    else:
        return x[1:]
    if x[3]%2=0:
        return x
    else:
        return x[:3]