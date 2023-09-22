def filtra_pares(t1):
    '''Calcula e retorna uma tupla apenas com os elementos pares e na mesma ordem da tupla original
    tupla -> tupla'''
    a,b,c,d = t1
    t2=()
    if a%2 == 0:
        t2 = t2+(a,)
    if b%2 == 0:
        t2 = t2+(b,)
    if c%2 == 0:
        t2 = t2+(c,)
    if d%2 == 0:
        t2 = t2+(d,)
        return t2