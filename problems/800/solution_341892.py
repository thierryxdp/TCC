def total(compras,produtos):
    """
    	Função que retorna o valor total dos itens da lista
        que estejam disponíveis nesta loja.
    	list,dict -> float
    """
    valor = 0
    for produtos in compras:
        valor = valor + produtos[compras] 
    
    return round(valor,2)