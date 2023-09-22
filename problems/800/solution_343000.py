def total(lista,produtos):

    
    """
    list,dict--->float
    
    """
    soma=0
    
    for i in lista:
        soma+=produtos[i]
        
    return round(soma,2)