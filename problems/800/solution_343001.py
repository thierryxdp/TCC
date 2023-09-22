def total(lista,produtos):

    
    """
    list,dict--->float
    Utiliza-se o for para que haja a busca de cada string presente na 
    lista, fazendo com que todos seus valores sejam buscados no
    dicionario de produtos. Faz-se sua soma e no final do código é 
    utilizado ainda o comando round,já que foi pedido
    """
    soma=0
    
    for i in lista:
        soma+=produtos[i]
        
    return round(soma,2)