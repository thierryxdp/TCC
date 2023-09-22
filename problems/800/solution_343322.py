def total(lista,dic):
    '''função que recebe uma lista e um dicionario(dic) conte
    uma lista de compras e preço de cada produto respectiva
    mente retorna o valor total dos itens da lista;lista,dic
    ->float'''
    indice=0
    resp=0
    for i in lista:
        if lista[indice] in dic:
            resp+=(dict.get(dic,lista[indice]))
        indice+=1
    return resp