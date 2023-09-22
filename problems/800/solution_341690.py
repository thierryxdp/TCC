def total(compras,produtos):
    """
    Função recebe uma lista de compras e um dicionário(produtos) contendo o preço
    de cada produto disponível em uma determinada loja, e retorna o valor total
    dos itens da lista que estejam disponíveis nesta loja.
    list, dict ->
    """
    valor=0
    for i in range(len(compras)):
        if compras[i] in produtos:
            valor+=produtos[compras[i]]
    return round(total,2)