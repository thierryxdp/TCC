def total(lis_compra,preco_produto):
    '''Recebe uma lista e um dicionário
    e retorna a soma dos preços dos elementos 
    da lista que existe no dicionário
    list,dict->int'''
    preco_total=0
    for i in lis_compra:
        if i in preco_produto:
            preco_total=round(preco_total+preco_produto[i],2)
    return preco_total