def total(lista,preco):
    '''Função que recebe uma lista de compras, um dicionario com itens disponiveis e seus valores
    retorna o valor total dos itens disponiveis pertecentes a lista
    list,dict->int'''
    i=0
    total=0
    for i in range(len(lista)):
        if lista[i] in list(dict.keys(preco)):
            total+=dict.get(preco,lista[i])
            i+=1
    return round(total,2)