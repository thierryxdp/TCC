def busca(matriz,busca):
    '''
    '''
    lista = []
    a = len(matriz)
    for i in range(a):
        for j in matriz[2]:
            if j == setor:
                lista.append(i)
    return lista