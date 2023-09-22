def total(lista, precos):
    '''Retorna o valor todal da compra dos produtos na lista a partir dos valores
    dos produtos em preços.
    list, dict - > float'''
    soma = 0

    for produto in lista:
        if produto in precos:
            soma = soma + precos[produto]

    return round(soma,2)