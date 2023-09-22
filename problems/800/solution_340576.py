def total (compras, mercado):
    pagar = {}
    for i in mercado:
        if mercado[i] in compras:
            pagar = pagar + mercado.pop(i)
    return pagar