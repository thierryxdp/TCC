def busca(setor,matriz):
    '''
    '''
    lista = []
    a = len(matriz)
    for i in range(a):
        for j in matriz[2]:
            if j == setor:
                lista.append(matriz[i])
    return lista