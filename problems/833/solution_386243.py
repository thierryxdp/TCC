def conta_numero4(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    lista_soma=[]
    for i in range(nlinhas):
        lista=[]
        for j in range(mcolunas):
            lista_soma.append(matriz[i][j])
    return lista_soma.count(numero)