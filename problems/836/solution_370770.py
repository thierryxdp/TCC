def busca(setor, matriz):
    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz)):
            if matriz[i][j] == setor:
                teste = True
        if teste == False:
            matriz.pop(matriz[i][j])
    if setor not in matriz[i]:
        return []     
    return matriz