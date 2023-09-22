def total(lista,dicionario):
    '''retorna o valor total de compras dada a lista de compras e o dicionario com o valor de cada produto; list,dict -> float'''
    lista_de_compras = []
    for item in lista:
        if item in dicionario:
            lista_de_compras = lista_de_compras + [dicionario[item],]
    return sum(lista_de_compras)