def total(lista,dic):
    '''função que contem uma lista de compras e um dicionario
    contendo o preço de cada produto de uma loja e retorna o valor
    totaldos itens da lista que estejam disponiveis nesta loja;
    list,dict->float'''
    x=0
    for elem in range(len(lista)):
        m=lista[elem]
        if m in dict.keys(dic):
            x=x+dict.get(dic,m)
    return round(x,2)