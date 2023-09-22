def total(listaDeCompra,precoProduto):
    """Dada uma lista de compras e um dicionário contendo
    o preço disponível na loja, a função calcula e retorna
    o valor total dos itens da lista que estejam disponíveis.
    Parametros de Entrasa: list, dict
    Retorna: float"""

    total=0
    
    for itens in listaDeCompra:
        if itens in precoProduto.keys():
            total= total+ precoProduto[itens]
    return round(total,2)