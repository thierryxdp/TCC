def busca(setor,matriz):
    ''' '''
    lista = []
    for s in range(len(matriz)):
        if setor in matriz[s]:
            list.remove(matriz[s],setor)
            lista = lista + [matriz[s]]
    return lista