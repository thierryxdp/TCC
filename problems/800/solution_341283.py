def total (lista_compras,preco):
    """Função que dada uma lista de compras e um dicionario
    contendo o preço de cada produto disponivel de uma 
    determinada loja, retorna o valor total dos itens da lista
    que estejam disponiveis nessa loja"""
    custo = 0
    for produtos in lista_compras:
        if produtos in preco:
            custo = custo + dict.get(preco,produtos)
    return round(custo,2)