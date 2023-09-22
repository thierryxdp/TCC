def total(ListaCompras,dicionarioMercado):
    '''retorna o preco em float de quanto se deve pagar baseado
    numa lista de compras e no preco de cada produto
    list,dict->float'''
    valor = 0
    for i in ListaCompras:
        if i in dicionarioMercado:
            valor += dicionarioMercado[i]
    return round(valor,2)