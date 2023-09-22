def busca(setor,matriz):
    lista=[]
    for i in range(0,3):
        if setor in matriz[i]:
            del matriz[i][2]
            list.append(lista,matriz[i])
    return lista