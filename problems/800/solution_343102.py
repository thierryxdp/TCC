def total(lista_compras,dicionario_precos):
    """
    Essa função, dados como argumentos uma lista contendo a lista de compras
    e um dicionario contendo o preço dos produtos, a função ira retornar o
    valor total das compras dos produtos disponiveis em uma determinada loja
    list,dict->float
    """
    lista_precos = []
    itens_disponiveis = list(dict.keys(dicionario_precos))
    for item in itens_disponiveis:
        if item in lista_compras:
            list.append(lista_precos,item)
    return round(sum(lista_precos),2)