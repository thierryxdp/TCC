def total(lista,produtos):

    
    """
    list,dict--->float
    
    """
    soma=0
    
    for i in produtos:
        soma+=produtos[i]+soma
        
        return soma