def total(lista,produtos):
    '''Função calcula total da lista de compras de acordo com 
    os preços do dicionário. list, dict --> float'''
    i = 0
    total = 0
    for elementos in lista:
        if lista[i] in produtos:
            total += 1 produtos[lista[i]]
            i+=1
    return round(total,2)