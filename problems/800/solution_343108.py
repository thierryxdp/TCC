def total(lista_compras,dicionario_precos):
    """
    Essa função, dados como argumentos uma lista contendo a lista de compras
    e um dicionario contendo o preço dos produtos, a função ira retornar o
    valor total das compras dos produtos disponiveis em uma determinada loja
    list,dict->float
    """
 
    itens_disponiveis = list(dict.keys(dicionario_precos))
    lista_precos = []
    
    for item in itens_disponiveis:
        if item in lista_compras:
            list.append(lista_precos,dicionario_precos[item]

            
    return lista_precos