def total(l,d):
    ''' retorna o valor total dos itens que estejam disponíveis nessa loja, dada uma lista de compras e um dicionário contendo o preço de cada disponível na loja;
    lis,dict -> float '''
    x = 0
    for elem in l:
        m = l(elem)
        if m in dict.keys(d):
            x = x + dict.get(d,m)
    return  round(x,2)