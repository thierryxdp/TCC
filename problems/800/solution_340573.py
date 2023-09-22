def total (compras, mercado):
    pagar = {}
    for i in mercado:
        if mercado[i] in compras:
            pagar.append(mercado[i])
    return pagar