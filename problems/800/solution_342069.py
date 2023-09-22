def total(x,y):
    '''A função recebe uma lista (x) de produtos encontrados em supermercados
    e também recebe um dicionário dos preços (y). Deverá retornar o valor
    total dos produtos citados na lista (x).
    
    lista, dicionário -> float'''
    
    soma = 0
    
    for produto in x:
        if x[produto] in y:
            soma = soma + y[x[produto]]
        
    return soma