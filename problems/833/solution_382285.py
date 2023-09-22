def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    for x in range(coluna*linha):
        lista.append(matriz[x])
    return lista