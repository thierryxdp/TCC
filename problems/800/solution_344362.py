def total(lista,dici):
    '''.'''
    soma = 0
    for produto in lista:
        if produto in dici:
            soma = soma + lista[produto]
    return soma