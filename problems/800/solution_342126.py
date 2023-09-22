def total(lista,dicionario):
    '''A função calcula o total dos preços dos itens de uma lista de compras'''
    l=[]
    i=0
    for n in range(len(lista)):
        if lista[i] in dict.keys(dicionario):
            list.append(l,dicionario[lista[i]])
        i=i+1
    return round(sum(1),2)