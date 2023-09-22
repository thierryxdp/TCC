def total(compras,precos):
    '''Funcao que recebe de entrada uma lista de compras e 
    um dicionario referente aos precos dos produtos de uma 
    loja. O retorno eh a soma dos valores dos produtos
    da lista de compras disponiveis para venda na loja.
    list, dict -> float'''
    valor_total = 0
    for produto in compras:
        if produto in precos:
            valor_total += precos[produto]
    return round(valor_total,2)