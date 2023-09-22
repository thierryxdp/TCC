def total(compras,preco):
    '''Uma função que recebe uma lista de compras
    e um dicionário com os preços do produto e retorna o total
    a ser gasto na compra
    lis,dict-->float'''
    total=0
    totalf=0
    for i in range(1,len(produtos)):
        if lista_comp[i] in produtos.keys():
            total=total+lista_comp[i]
            totalf=round(total,2)
        return totalf