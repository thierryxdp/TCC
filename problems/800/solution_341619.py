def total (compras, mercado):
    ''''retorna o valor de uma lista de comprar, dado o valor dos produtos
    lista, dicionario -> float'''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)