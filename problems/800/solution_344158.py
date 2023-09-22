def total(l_c,preco):
    '''função em que dada uma lista de compras e um dicionário contendo o preço
    de cada produto diusponível em uma determinada loja retorne o valor total
    dos itens da lista que estejam disponíveis nesta loja;
    list, dict -> float'''
    v=0
    for i in l_c:
        if i in preco:
            v+=preco[i]
    return round(v,2)