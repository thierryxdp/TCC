def busca(setor, matriz):
    r=[]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            z = matriz[i][:2]+matriz[i][3:]
    return r