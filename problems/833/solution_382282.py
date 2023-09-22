def conta_numero(numero,matriz):
    lista = []
    coluna = len(matriz[0])
    linha = len(matriz)
    for x in range(0,coluna*linha):
        if x==numero:
            lista.append(x)
    return lista