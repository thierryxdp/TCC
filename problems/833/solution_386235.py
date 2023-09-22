def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    novalista=[]
    for i in range(nlinhas):
        for j in range(mcolunas):
            novalista=matriz[0]+matriz[1]+matriz[2]
            novalista.append(numero)
    return novalista.count(numero)