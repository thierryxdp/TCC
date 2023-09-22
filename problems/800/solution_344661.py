def total(lista_compras, produtos):
    "função calcula total da lista de compras de acordo com os preços do dicionário list, dict --> float"

    contagem = 0
    valor_total = 0
    limit = len(lista_compras)
    while contagem < limit:
        valor_total += produtos[lista_compras[contagem]]
        contagem += 1
        valor_total = round(valor_total, 2)
    return valor_total