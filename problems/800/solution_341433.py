def total(lista_compras, produtos):
    """
    Retorna o preço total das compras.
    list, dict -> float
    """
	s=0
    for n in range(0,len(lista_compras)):
    	s += round(dict.get(produtos, lista_compras[n]),2)