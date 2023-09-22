def filtra_pares(tupla):
    """ Funcao recebe uma tupla com quatro elementos inteiros e retorna uma
    nova tupla com apenas os elemtnos pares da tupla original, na mesma
    ordem em que se encontravam """
    
    n1, n2, n3, n4 = tupla
    
    n_tupla = ()
    
    if n1%2 == 0:
        n_tupla = n_tupla + (n1,)
    else:
        n_tupla
    
    if n2%2 == 0:
        n_tupla = n_tupla + (n2,)
    else:
        n_tupla
        
    if n3%2 == 0:
        n_tupla = n_tupla + (n3,)
    else:
        n_tupla
        
    if n4%2 == 0:
        n_tupla = n_tupla + (n4,)
    else:
        n_tupla
        
    return n_tupla