def total(compras, dic):
    ''' retorna o valor total da compra'''
    s = sum( [dic[i] for i in compras] )
    return round(s, 2)