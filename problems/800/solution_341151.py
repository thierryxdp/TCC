def total(lista,dici):
    '''Retorna o valor das compras de uma lista de compras, arredondando 2 casas. list,dict->float'''
    tudo=0
    for item in lista:
        if item in dici:
            tudo=tudo+float(dici[item])
    return round(tudo,2)