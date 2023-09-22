def total(lista,dicio):
    compras = 0
    for palavra in lista:
        if palavra in dicio:
            compras += dicio.get(palavra)
    return round(compras)