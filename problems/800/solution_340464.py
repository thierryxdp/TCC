def total(lista_compras,produtos):
    """dadas uma lista de compras e um dicionário contendo o preço de cada produto
    disponível em uma determinada loja, a função retorna o valor total dos itens
    lista que estejam disponíveis na loja;
    list,dict->float"""
    produtos_disponíveis=[]
    soma_precos=0
    for produto in lista_compras:
        if produto in produtos:
            soma_precos=soma_precos+(dict.get(produtos,produto))
    return soma_precos