def total(lista, produtos):
    '''Esta função calcula o total da lista de compras'
    list, dict -- > float'''
    cnt = 0
    total1 = 0
    for elementos in lista:
        if lista[cnt] in produtos:
            total1 += produtos[lista[cnt]]
            cnt += 1
    return round(total1,2)