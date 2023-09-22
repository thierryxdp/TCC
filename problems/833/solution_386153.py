def conta_numero(numero,matriz):
    ''''''
    nv_matriz=[]
    
    for linha in matriz:
        nv_linha=linha[:]
        nv_matriz=nv_matriz+[nv_linha]
        
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            nv_matriz[i][j]=nv_matriz[i][j]
    return list.count(nv_matriz,numero)