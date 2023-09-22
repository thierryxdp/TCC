def busca(elemento,matriz):
    lin = len(matriz)
    col = len(matriz[2])
    resp= []
    for i in range(0,lin): 
        if elemento in matriz[i][3]:
            list.append(resp,matriz[i])
    return resp