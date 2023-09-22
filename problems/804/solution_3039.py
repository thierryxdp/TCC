#Start your python function here
def filtra_pares (numeros):
    """ Recebe quatro numeros e e filtra os numeros que são pares,
    excluindo os não pares.
    tupla -> tupla"""
    n1, n2, n3, n4 = numeros
    pares = tuple ()
    
    if n1 % 2 == 0:
        pares += (n1, )
    
    if n2 % 2 == 0:
        pares += (n2, )
    
    if n3 % 2 == 0:
        pares += (n3, )
    
    if n4 % 2 == 0:
        pares += (n4, )
        
    return pares