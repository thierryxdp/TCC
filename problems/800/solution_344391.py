def total(compras, dicio):
    '''função que recebe uma lista de compras e um dicionário com o valor dos produtos e retorna o total gasto
    list, dict-> float'''
    
    valor=[]
    
    for i in dicio:
        if i in compras:
            list.append(valor,compras[i])
    
    return valor