def filtra_pares(tup):
    '''
    retorna os pares da tupla
    tuple -> tuple 
    '''
    a=tup[0]
    b=tup[1]
    c=tup[2]
    d=tup[3]
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a+b+c+d