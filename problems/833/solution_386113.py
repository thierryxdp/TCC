def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        lista=[]
        for j in range(mcolunas):
            if numero in matriz[i][j]:
                lista.append(matriz[i][j].count(numero))
    return lista.pop()