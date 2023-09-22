def busca(matriz,setor):
    lista=[]
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            if matriz[c][i]==setor:
                lista.append(matriz[c])
    for m in range(len(lista)):
        del lista[m][2]
    return lista