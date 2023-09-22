def busca(setor, matriz):
    r=[]
    for i in range(len(matriz)):
        if matriz[i][1] == setor:
            z = matriz[i][:1]+matriz[i][3:]
    return r