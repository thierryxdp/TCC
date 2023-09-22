def total(lista_compras, valores):
    total=0
    i=0
    if lista_compras[i] in valores.keys():
        x=valores.values()
        total= total + x
    return total