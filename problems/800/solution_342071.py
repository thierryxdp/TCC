def total(x,y):
    '''A função recebe uma lista (x) de produtos encontrados em supermercados
    e também recebe um dicionário dos preços (y). Deverá retornar o valor
    total dos produtos citados na lista (x).
    
    lista, dicionário -> float'''
    
    soma = 0
    
    for produto in x:
        if produto in y:
            a = y[produto]
            soma = soma + a
        
    return round(soma,2)