def total(lista,tabela):
    """Função que dada uma lista de compras e um dicionário contendo o preço de cada produto em uma loja, retorna o valor total dos itens da lista disponíveis na loja. list -> int"""
    lista = list(lista)
    total = 0
    for t in range(len(lista)):
        total = total + (tabela[lista[t]])
    return round(total,2)