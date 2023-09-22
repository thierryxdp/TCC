def total(compras, produtos):
    """Dada uma lista de compras (compras) e um dicionário contendo
    os produtos disponíveis na loja e seus preços (produtos), a função irá
	checar se o produto que está na lista, está também disponível na loja
    e irá somar o valor total das compras com base no valor dos produtos.
    Tipo da variável compras: list
    Tipo da variável produtos: dictionary
    Tipo da saída: float"""
    valor_compras = 0
    for contador in range(len(compras)):
        if compras[contador] in produtos:
            valor_compras = valor_compras + produtos[compras[contador]]
	return round(valor_compras, 2)