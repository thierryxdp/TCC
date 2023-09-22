def busca(setor,matriz):
    ''' '''
    lista = []
    for s in range(len(matriz)):
        if setor in s:
            lista = lista + [s]
    return lista