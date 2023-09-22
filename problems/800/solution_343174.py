def total(lista,produtos):
    '''Dado uma lista de compras, e um dicionário contendo o preço de cada produto disponivel, retorna um valor total de acordo com os produtos da lista de compras que tem na loja
    list,dict->int'''
    total=0
    for i in range(len(lista)):
        if lista[i] in produtos:
            total=total+(dict.get(produtos,lista[i],0))
            
    return total