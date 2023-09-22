def filtra_pares(tupla):
    """Mostra os elementos pares da tupla de elementos inteiros
    	tuple -> tuple
    	Parameters:
        tupla: Tupla com quatro elementos inteiros
        
        Returns:
        Os elementos pares da tupla de quatro elementos inteiros fornecida
     """
    item1, item2, item3, item4 = tupla
    
    if item1%2 == 0:
        item1 == True
    else:
        item1 = False
    if item2%2 == 0:
        item2 == True
    else:
        item2 = False
    if item3%2 == 0:
        item3 == True
    else:
        item3 = False
    if item4%2 == 0:
        item4 == True
    else:
        item4 = False
        
    pares = filter(None,(item1,item2,item3,item4))
    
    return (tuple(pares))