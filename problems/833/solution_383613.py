def conta_numero(numero, matriz):
    lista = []
    for i in matriz:
        for j in i:
            lista.append(j)
    return lista.count(numero)