def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    novalista=[]
    for i in range(nlinhas):
        for j in range(mcolunas):
            novalista=matriz[i]+matriz[j]
            novalista.append(numero)
    return novalista.count(numero)