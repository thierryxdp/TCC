def total (lista, dicionario):
    """Retorna o valor total de uma dada lista de compras com base num dado dicionário com os preços dos produtos disponíveis.
    Entrada: list, dict
    Saída: float
    """
    compras = []
    x = 0
    for i in range(len(lista)):
        if lista[x] in dict.keys(dicionario):
            list.append (compras, dicionario[lista[x]])
        x += 1
    return round(sum(compras),2)