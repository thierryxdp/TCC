def total(lista_compras, precos):
    """Função que dada uma lista de compras e um dicionário
    que contenha o valor de cada produto, retorna o valor
    total dos itens da lista que estejam disponíveis;
    list, dic -> float"""
    total_t = 0.0
    for produto in precos:
        if produto in precos:
            total_t = total_t + precos[produto]
    return total_t