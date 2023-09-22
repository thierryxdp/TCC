def total(l,d)
    '''Função que retorna o valor total dos itens dado uma 
    lista de compras e um diconário contendo o preço
    de cada item.
    list, dict -> int'''
    preco_total = 0
    for p in l:
        preco_total +=dict.get(d,p,0)
    return round(preco_total,2)