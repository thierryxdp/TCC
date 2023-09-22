def total(lista, dicio):
    '''funcao que soma os produtos dados na lista de compra.
    list, dict-> float'''
    total = 0
    for palavra in lista:
        if palavra in dicio.keys():
            total = total + dicio.get(palavra)
    return round(total,2)