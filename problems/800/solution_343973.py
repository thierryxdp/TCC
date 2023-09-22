def total(lista_de_compras,produtos):
    ''' Essa função calcula o valor total de produtos referentes a uma lista de compras
    list,dict->float'''
    soma=0
    for x in lista_de_compras:
        if x in dict.keys(produtos):
            soma+=dict.get(produtos,x)
    return soma