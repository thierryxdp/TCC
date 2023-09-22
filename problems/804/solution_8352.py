def filtra_pares(t):
    '''Recebe uma tupla de 4 elementos como entrada e retorna uma nova tupla contendo
    apenas os elementos pares, na mesma ordem em que encontravam;
    tupla -> tupla'''
    if t[0:1]%2==0:
        return t[0:1]
    if t[1:2]%2==0:
        return t[1:2]
    if t[2:3]%2==0:
        return t[2:3]
    if t[3:]%2==0:
        return t[3:]