def total(lista_compras, precos):
    """Recebe uma lista de compras e um dicionário com os preços de cada
produto, e retorna o valor total dos itens da lista que estejam
disponíveis na loja;
list, dic -> float"""
    valor = 0

    for item in lista_compras:
        if item in precos:
            valor = valor + precos[item]
            
    return  round(valor, 2)