def total(lista, preços):
    '''Retorna o valor todal da compra dos produtos na lista a partir dos valores
    dos produtos em preços.
    list, dict - > float'''
    soma = 0

    for produto in lista:
        if produto in preços:
            soma = soma + preços[produto]

    return round(soma,2)