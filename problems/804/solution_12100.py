def par(x):
    '''retorna se um numero é par ou não;
    int -> bool'''
    return x%2==0
def filtra_pares(a,b,c,d):
    '''retorna um conjunto com apenas os 
    numeros pares contidos no conjunto inicial;
    tuple -> tuple'''
    pares=()
    if par(a):
        pares=pares + (a,)
    else:
        pares=pares
    if par(b):
        pares=pares + (b,)
    else:
        pares=pares
    if par(c):
        pares=pares + (c,)
    else:
        pares=pares
    if par(d):
        pares=pares + (d,)
    else:
        pares=pares
    return pares