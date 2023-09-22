def total (compras, mercado):
    ''''retorna o valor de uma lista de compras(ldc) baseado em um dicionário
    (mercado)
    list -> dict'''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)