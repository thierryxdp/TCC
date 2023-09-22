def total (compras, mercado):
    valor = {}
    for i in mercado:
        if compras in mercado:
            valor.append(i)
    return valor