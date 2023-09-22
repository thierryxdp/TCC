def total(lista_compras, precos):
    """Função que dada uma lista de compras e um dicionário
    que contenha o valor de cada produto, retorna o valor
    total dos itens da lista que estejam disponíveis;
    list, dic -> float"""
    v_total = 0.0
    for produto in precos:
        if produto in precos:
            v_total = v_total + precos[produto]
    return v_total