def total(lista_compras, precos):
    '''calcule uma funcao que receba ums lista de compras e um dicionario com os precos dos produtos, e retorne o valor totat dos itens da lista. list, dict --> float'''
    valor_total= 0
    for produto in lista_compras:
        if produto in precos:
            valor_total = valor_total + precos[produto]
    return round(valor_total,2)