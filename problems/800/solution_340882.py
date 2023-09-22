def total (lista_compras, valores):
    '''
    '''
    valor_total = 0
    for produto in lista_compras:
        if produto in valores:
            valor_total = valor_total + round(valores[produto],2)
    return valor_total