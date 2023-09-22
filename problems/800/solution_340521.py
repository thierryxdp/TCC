def total(lista, relation):
    """A função recebe uma lista de compras e uma relação
	de produtos contendo o preço de cada produto disponível
	na loja, e retorna o valor total dos itens da lista que
	estejam disponíveis;
	list, dict --> int"""
    listprod = list(dict.keys(relation))
    valor = 0
    for n in listprod:
        if n in lista:
            valor += dict.get(relation, n)
    return round(valor, 2)