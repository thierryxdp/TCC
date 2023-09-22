def total(lista, dicionario):
    """A Entrada será uma lista e um dicionário com o preço
    de diversos elementos, com seus nomes associados. 
    O retorno será a soma dos preços dos produtos do dicionário
    que estiverem na lista com até dois números decimais"""
    #list, dici -> num
    
    total = 0
    for produtos in lista:
        if produtos in dicionario:
            total = total + dicionario(produtos)
    return round(total, 2)