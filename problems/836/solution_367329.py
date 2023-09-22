def busca(setor,matriz):
    ''' '''
    lista=[]
    for n in range(len(matriz)):
        if setor == matriz[n][2]:
            list.remove(matriz[n],setor)
            lista = lista + [matriz[n]]
    return lista