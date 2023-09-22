def filtra_pares(tupla):
    """Mostra os elementos pares da tupla de elementos inteiros
    	tuple -> tuple
    	Parameters:
        tupla: Tupla com quatro elementos inteiros
        
        Returns:
        Os elementos pares da tupla de quatro elementos inteiros fornecida
     """
    item1, item2, item3, item4 = tupla
    
    if item1, item2, item3, item4%2 == 0:
        return True
    else:
        return False
         
    pares = filter(None,tupla)
    
    return (tuple(pares))