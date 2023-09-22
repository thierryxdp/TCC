def total(lista, dicionario):
    """funcao que retorna o valor de uma lista de compras com base em um dicionario dado com os preços do produtos.
    list, dict -> float"""
    compras = []
    x = 0
    for n in range(len(lista)):
        if lista[x] in dict.keys(dicionario):
            list.append (compras, dicionario[lista[x]])
            x += 1
    return round(sum(compras),2)