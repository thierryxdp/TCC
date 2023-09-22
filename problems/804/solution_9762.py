def filtra_pares(filtragem):
    ''' Dado uma tupla com 4 elementos inteiros,
    retorna uma nova tupla apenas com os pares da original,
    na mesma ordem
    tupla(int,int,int,int) -> tupla'''
    
    t1 = list(filtragem)\
    for n in t1:
        if n % 2 != 0:
            t1.remove(n)
    t2 = t1
    for n in t2:
        if n % 2 != 0:
            t2.remove(n)
    t3 = t2
    for n in t3:
        if n % 2!= 0:
            t3.remove(n)
    t4 = tuple(t3)
    return t4