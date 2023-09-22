def total(compras,preco):
    '''Uma função que recebe uma lista de compras
    e um dicionário com os preços do produto e retorna o total
    a ser gasto na compra
    lis,dict-->float'''
    soma=0
    for n in preco:
        if compras in preco:
            soma=soma+[n]
    return soma