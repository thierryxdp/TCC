"""Dados 4 inteiros em uma tupla, esta função retorna uma nova tupla contendo
apenas os elementos inteiros, na mesma ordem em que foram informados."""
def filtra_pares((a,b,c,d)):
    ''' tupla(int, int, int, int) -> tupla'''
    pares = ()
    
    if (a%2 ==0):
        pares = pares + (a,)
    
    if (b%2 ==0):
        pares = pares + (b,)
    
    if (c%2 ==0):
        pares = pares + (c,)
    
    if (d%2 == 0):
        pares = pares + (d,)
    
    return pares