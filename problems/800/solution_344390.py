def total(compras, dicio):
    '''função que recebe uma lista de compras e um dicionário com os preços dos produtos e retorna o valor gasto
    list, dict-> float'''
    
    valor=[]
    
    for i in compras:
        if i in dicio:
            valor=dicio[i]
        i=i+1
    return valor