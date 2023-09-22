def total(compras,preco):
    '''Uma função que recebe uma lista de compras
    e um dicionário com os preços do produto e retorna o total
    a ser gasto na compra
    lis,dict-->float'''
    x=0
    total=0
    preco=preco.items()
    for i in range(0,len(preco)):
        if compras[i] in preco.keys():
            total=total+preco[i]
        return total