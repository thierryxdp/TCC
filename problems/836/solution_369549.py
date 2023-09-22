def busca(setor,matriz):
    '''
    '''
    lista = []
    a = len(matriz)
    for i in range(a):
        for j in matriz[i]:
            if j == setor:
                lista.append(matriz[i])
                del lista[i-1][2]
    return lista