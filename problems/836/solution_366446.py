def busca(setor,matriz):
    '''A função recebe uma matriz busca por um determinado setor dessa matriz e retorna todas as informações referentes ao funcionário desse setor.
    string,lista->lista'''
    lista = []
    for s in range(len(matriz)):
        if setor in matriz[s]:
            list.remove(matriz[s],setor)
            lista = lista + [matriz[s]]
    return lista