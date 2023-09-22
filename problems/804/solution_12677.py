import math
def filtra_pares (numeros):
    '''tuple -> tuple'''
    pares = ()
    
    for n in numeros:
        if n % 2 ==0:
            pares + = (n[0],)
            
    return pares