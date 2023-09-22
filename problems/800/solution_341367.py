def total(lista_de_compras,produtos):
    """retorna o valor da compra de acordo com os itens da lista e os produtos do mercado; list, dict -> float"""
    a=0
    for x in lista_de_compras:
        a=a+produtos[x]
    return round(a,2)