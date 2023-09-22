def busca(setor,matriz):
    l=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(l,matriz[i])
            list.remove(l,setor)
    return l