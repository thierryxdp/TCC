def busca(setor,matriz):
    ''' '''
    for i in range(len(matriz)):
        if setor in matriz[i]:
            return matriz[i]
        else:
            return []