def total(lista, produtos):
    '''Recebe uma lista de produtos e um
    dicionario contendo o preço de cada 
    produto disponivel e retorna o valor
    total dos itens da lista
    
    list, dict -> float
    '''
    
    contador = 0
    total = 0
    
    for elementos in lista:
        if lista[contador] in produtos:
            total += produtos[lista[contador]]
            contador += 1
    return round(total, 2)