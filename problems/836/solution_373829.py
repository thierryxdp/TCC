def busca(setor, matriz):
    resultado = []
    n = len(matriz)
    for i in range(n):
        if(setor==matriz[i][2]):
            resultado.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return resultado