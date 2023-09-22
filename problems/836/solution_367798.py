def busca(matriz,setor):
    f=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            f.append(matriz[i])
    return f