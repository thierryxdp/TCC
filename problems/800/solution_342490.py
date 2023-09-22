def total (lista,dicio):
    '''
    função que dada uma lista e um dicionário com os preços de cada produto na lista, retorna
    o total da compra de cada elemento baseado no preço de cada no dicionario, somando zero ao total
    caso o produto não tenha na loja
    list,dict-->float
    '''
  
    soma_compras=0

    for el in lista:
        if el in dicio:
            soma_compras= soma_compras+ dicio[el]
        if el not in dicio:
            soma_compras= soma_compras+0
    return round(soma_compras,2)