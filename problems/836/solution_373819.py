def busca(matriz, setor):
     P = matriz()
    resultado = []
    n = len(P)
    for i in range(n):
        if(P[i][2]==setor):
            resultado.append([P[i][0],P[i][1],P[i][3]])
    return resultado