def total(lista_compras, lista_disponivel):
    preco_total = 0
    for item in lista_compras:
        """ Buscando a ocorrencia dos itens contidos na lista de compras em lista de disponiveis """
        if item in lista_disponivel.keys():
            """ Caso exista ocorrencia, fazendo somátoria dos valores """
            preco_total += lista_disponivel[item]
    return round(preco_total,2)