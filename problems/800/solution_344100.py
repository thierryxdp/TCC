def total(lista, produtos):
    '''funcao calcula total da lista de compras de acordo com os precos do dicionario'''
    '''list, dict--> float'''
    contador = 0 
    total = 0 
    for elements in lista:
        if lista[contador] in produtos:
            total += produtos[lista[contador]]
            contador += 1
    return round(total, 2)