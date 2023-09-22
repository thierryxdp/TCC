def filtra_pares(a,b,c,d):
    """função que recebe 4 elementos de uma tupla e retorna
    uma nova tupla apenas com os elementos pares
    tupla -> tupla"""
    t=(a,b,c,d)
    for t[i] in t:
        if i%2==0:
            return (i, )