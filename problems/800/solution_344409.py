def total(compras,dicio):
    '''função que recebe uma lista de compras e um dicionário de preços
    e retorna o valor gasto
    list,dict->float'''
    
    soma=0
    
    for i in compras:
        soma=soma+dicio[i]
    
    return round(soma,2)