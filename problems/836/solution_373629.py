def busca(elemento,matriz):
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if elemento in matriz[i][j]:
                lista.append(matriz[i])
    for k in lista:
        for o in k:
            if o==elemento:
                indice=k.index(elemento)
                del k[indice]
    return lista