def total(lista, precos):
    """Função que dada uma lista de compras e um dicionário
    que contenha o valor de cada produto, retorna o valor
    total dos itens da lista que estejam disponíveis;
    list, dic -> float"""
    total = 0.0
    for produto in precos:
        if produto in precos:
            total = total + precos[produto]
    return total