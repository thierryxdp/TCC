def busca(matriz,setor):
    resultado = []
    n = len(matriz)
    for i in range(n):
        if(matriz[i][2]=setor):
            resultado.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return resultado