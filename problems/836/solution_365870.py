def busca(setor,matriz):
    ''' '''
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista,matriz[i])
            list.remove(matriz[i],setor)
    return lista