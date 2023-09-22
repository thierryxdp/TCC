def melhor_volta(matriz):
    nlin=len(matriz)
    ncol=len(matriz[0])
    menores=[]
    for i in range(nlin):
        menor=min(matriz[i])
        menores.append(menor)
        menores+=min(menores)
        for j in range(ncol):
    return menores