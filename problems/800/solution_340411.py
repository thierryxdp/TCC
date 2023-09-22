def total(lista, precos):
    '''ao receber uma lista de compras e um dicionário
    contendo o preço de cada produto disponível na loja,
    retorna o valor total dos itens da lista que estão
    dispoíveis nesta loja.
    list, dict -> float'''
    soma = 0
    for num in lista:
        if num in precos:
            soma = soma + precos[num]
    return round(soma, 2)