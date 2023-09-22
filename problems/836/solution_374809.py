def busca(matriz,busca_setor):
    '''Função que recebe uma matriz e retorna os dados
    de todos os funcionarios de um setor.
    list,str -> list
    '''
    lista = []

    for m in range(len(matriz)):
        if busca_setor in matriz[m]:
            lista.append(matriz[m])

    for m1 in range(len(lista)):
        if lista[m1][2] == busca_setor:
            del lista[m1][2]
            
    return lista