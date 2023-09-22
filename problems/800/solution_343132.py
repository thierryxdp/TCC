def total(lista_compras, valores):
    total=0
    for i in len(lista_compras):
        if lista_compras[i] in valores.keys():
            total= total + valores.values()
    return total