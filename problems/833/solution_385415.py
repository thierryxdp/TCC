def conta_numero(numero, matriz):
    lista = 0
    rep = 0
    while lista < len(matriz):
        rep = rep + list.count(matriz[lista],numero)
        lista = lista + 1
    return rep