def total(compras,precos):
    """funcao que dada uma lista de compras e um dicionario contendo os preços dos produtos disponiveis nessa loja, retorna o valor total referente aos itens que a da lista de compras
    list(str),dict(str:float)--->float"""
    preco_total=0
    for elem in range(len(compras)):
        if compras[elem] in precos:
            preco_total=preco_total+precos[compras[elem]]
    return round(preco_total,2)