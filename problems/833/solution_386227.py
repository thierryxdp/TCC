def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        novalista=[]
        for j in range(mcolunas):
            novalista=matriz[i][j]
            novalista.append(numero)
    return novalista.count(numero)