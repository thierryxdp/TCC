def total(lista_de_compras, dict_precos):
    """Recebe uma lista de compras e um dicionário com o preço de cada
    produto e retorna o valor total da lista dos itens que serão
    comprados e estão disponíveis na loja;
    list, dict -> float"""
    valor_total = 0
    for item in lista_de_compras:
        if item in dict_precos.keys():
            valor_total += dict_precos.get(item)
    return valor_total