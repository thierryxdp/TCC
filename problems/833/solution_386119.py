def conta_numero(numero,matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        for j in range(mcolunas):
            lista=[]
            if numero in matriz:
                lista.append(matriz.count(numero))
    return lista.pop()