def conta_numero(num, matriz):
    lista = []
    for x in matriz:
        for y in x:
            lista.append(y)
    return lista.count(num)