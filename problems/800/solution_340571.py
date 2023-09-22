def total (compras, mercado):
    pagar = {}
    for i in mercado:
        if mercado[i] in compras:
            levar = mercado[i]
            pagar.append(levar)
    return pagar