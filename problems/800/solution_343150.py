def total(lista_compras, valores):
    '''retorna o valor da lista de compras
    list,dict -> int'''
    total=0
    i=0
    for i in range(0,len(lista_compras)):
        if lista_compras[i] in valores.keys():
            total=valores[lista_compras[i]]+total
    return round(total,2)