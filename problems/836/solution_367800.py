def busca(setor,matriz):
    f=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            f.append(matriz[i][:2]+matriz[i][2:])
    return f