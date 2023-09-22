def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    lista_soma=[]
    if numero==0 and len(matriz[0])==0:
        return 0
    for i in range(nlinhas):
        lista=[]
        for j in range(mcolunas):
            lista_soma.append(matriz[i][j])
    return lista_soma.count(numero)