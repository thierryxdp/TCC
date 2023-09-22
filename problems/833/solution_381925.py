def conta_numero (n, matriz):
    mat = str.split(matriz)
    ocorrencias = []
    for n in mat:
        qtd = 0
        for c in mat:
            if c == n:
                qtd = qtd + 1
        list.append(ocorrencias, qtd)
    return ocorrencias