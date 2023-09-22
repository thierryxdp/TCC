def total(lista,dicionario):
    ''' dada uma lista de compras e um dicionario contendo o preço de cada produto.
calcula e retorna o valor total dos itens da lista presentes no dicionario.
list,dict->int'''
    j=0
    for x in lista:
        if x in dicionario:
            j= j+round(dicionario[x])
    return j