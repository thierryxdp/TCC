def total(lista,dici):
    '''.'''
    soma = 0
    for produto in lista:
        if produto in dici:
            soma = soma + dici[produto]
    return round(soma,2)