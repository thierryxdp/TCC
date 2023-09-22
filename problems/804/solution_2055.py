"""Dados 4 inteiros em uma tupla, esta função retorna uma nova tupla contendo
apenas os elementos inteiros, na mesma ordem em que foram informados."""
def filtra_pares(tupla_ent):
    ''' tupla(int, int, int, int) -> tupla'''
    pares = ()
    
    if (tupla_ent(0)%2 ==0):
        pares = pares + (tupla_ent(0),)
    
    if (tupla_ent(1)%2 ==0):
        pares = pares + (tupla_ent(1),)
    
    if (c%2 ==0):
        pares = pares + (c,)
    
    if (d%2 == 0):
        pares = pares + (d,)
    
    return pares