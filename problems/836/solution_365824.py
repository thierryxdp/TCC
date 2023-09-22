def busca(setor,matriz):
    l=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            list.append(l,matriz[i])
    return l