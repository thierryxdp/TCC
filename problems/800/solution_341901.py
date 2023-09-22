def total(compras,preco):
    '''Uma função que recebe uma lista de compras
    e um dicionário com os preços do produto e retorna o total
    a ser gasto na compra
    lis,dict-->float'''
    soma=0
    for n in preco:
        if compras[n] in preco:
            soma=soma+preco[n]
    return soma