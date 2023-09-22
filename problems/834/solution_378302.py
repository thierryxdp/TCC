def media_matriz(P):
    lista=[]
    for i in P:
        for j in i:
            lista.append(j)
    col=len(P[0])
    lin = len(P)
    relacao = lin * col
    return sum(lista)/relacao