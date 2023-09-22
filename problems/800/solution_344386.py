def total(compras, dicio):
    '''função que recebe uma lista de compras e um dicionário com os preços dos produtos e retorna o valor gasto
    list, dict-> float'''
    
    for i in compras:
        if compras in dicio:
            valor=dicio[compras]
    return valor