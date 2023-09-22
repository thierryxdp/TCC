def busca(setor,matriz):
    '''recebe uma matriz e faz uma busca por setor e retorna os dados de todos os funcionários daquele setor.'''
    lista=[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.remove(matriz[i],setor)
            list.append(lista,matriz[i])
    return lista