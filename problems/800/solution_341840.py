def total(compras,preco):
    '''Uma função que recebe uma lista de compras
    e um dicionário com os preços do produto e retorna o total
    a ser gasto na compra
    lis,dict-->float'''
    x=0
    total=0
    for i in range(1,len(preco)):
        if compras[i] in preco.keys():
            x = preco.values()[i]
        return x