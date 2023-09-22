def total (compras, mercado):
    ''''funcao que dada uma lista de compras e um dicionário(mercado) de preços de cada produto disponível, retorna o valor dos itens da lista disponíveis.'''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)