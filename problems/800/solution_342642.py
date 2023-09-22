def total(lista,dicio):
    ''' função que soma o preço de uma lista de produtos com os valores associados no dicio
    list,dict-->float'''
    valor=0
    for i in lista:
        if i in dicio:
            valor+= dicio[i]
    return round(valor,2)