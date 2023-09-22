def total(lista, produtos):
    ''' função que recebe uma lista  e dicionario, e retorna o valor total dos itens da lista
    list, dict -> float
    '''
    i = 0
    total = 0
    for produto in lista:
        if lista[i] in produtos:
            total += produtos[lista[i]]
            i+= 1
    return round(numero, 2)