def busca(setor,matriz):
    f=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            matriz[i].remove(matriz[i][2])
            f.append(matriz[i])
            
    return f