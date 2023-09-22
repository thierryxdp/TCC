def busca(setor,matriz):
    lista=[]
    indice=0
    for l in matriz:
        if matriz[indice][2]==setor:
            list.remove(matriz[indice],setor)
            list.append(lista,matriz[indice])
        indice=indice+1
    return lista