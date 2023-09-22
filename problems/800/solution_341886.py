def total(compras,produtos):
    """
    	Função que retorna o valor total dos itens da lista
        que estejam disponíveis nesta loja.
    	list,dict -> float
    """
    valor = 0
    for tudo in produtos:
        if compras in tudo:
            valor = valor + produtos[compras]    
    return valor