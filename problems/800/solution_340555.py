def total(lista,dicionario):
    compras = 0
    for produto in lista:
        if produto in dicionario:
            compras = compras + dicionario[produto]
        else:
            compras = compras
    return compras.format("%.2f")