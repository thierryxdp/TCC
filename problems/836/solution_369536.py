def busca(matriz,busca):
    '''
    '''
    lista = []
    for i in matriz:
        for j in range(i[2]):
            if j == setor:
                lista.append(i)
    return lista