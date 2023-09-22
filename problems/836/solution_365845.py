def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            list.append(lista,matriz[i])
    return lista