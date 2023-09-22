def total(lista_compras,dicio_precos):
    """
    	Retorna o valor total dos itens da lista inserida que estão no dicionário dado
    	list, dict -> float
    """
    valor_total=0.00
    for i in range(len(lista_compras)):
        if lista_compras[i] in dicio_precos:
        	valor_total += dicio_precos[lista_compras[i]]
    return valor_total