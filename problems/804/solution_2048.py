"""Dados 4 inteiros em uma tupla, esta função retorna uma nova tupla contendo
apenas os elementos inteiros, na mesma ordem em que foram informados."""
def filtra_pares(tupla):
    ''' (int, int, int, int) -> tupla'''
	pares = ()
    
    if (tupla(0)%2 ==0):
        pares = pares + (tupla(0),)
    
    if (tupla(1)%2 ==0):
        pares = pares + (tupla(1),)
    
    if (tupla(2)%2 ==0):
        pares = pares + (tupla(2),)
    
    if (tupla(3)%2 == 0):
        pares = pares + (tupla(3),)
    
    return pares