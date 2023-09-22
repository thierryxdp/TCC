def total(lista_compras, valores):
    i=0
    total=0
    for i in len(lista_compras):
        if lista_compras[i] in valores.keys():
            total= total + valores.values()
    return total