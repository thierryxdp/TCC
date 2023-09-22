def total(lista,produtos):

    
    """
    list,dict--->float
    
    """
    soma=0
    
    for i in range(len(produtos)):
        soma+=produtos[i]+soma
        
        return soma