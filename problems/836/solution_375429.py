def busca(procura,matriz):
    lista=[]
    for i in range(len(matriz)):
        if procura in matriz[i]:
            lista.append(matriz[i])
            matriz[i].pop(2)
    return lista