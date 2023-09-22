def busca(elemento,matriz):
    lista=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j])
            if elemento in linha:
                indice=linha.index(elemento)
                del linha[indice]
        lista.append(linha)
    return lista