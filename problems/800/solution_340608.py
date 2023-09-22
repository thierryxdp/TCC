def total(lista, produtos):
    '''função calcula total da lista de compras
    de acordo com os preços do dicionário
    list, dict--> float'''

    contador = 0
    total = 0
    
    for elementos in lista:
        if lista[contador] in produtos:
            total += produtos[lista[contador]]
            contador += 1

    return round(total, 2)