def busca(matriz,busca_setor):
    '''Função que recebe uma matriz e retorna os dados
    de todos os funcionarios de um setor.
    list,str -> list
    '''
    lista_dados = []

    for m in range(len(matriz)):
        if busca_setor in matriz[m]:
            lista_dados.append(matriz[m])

    for m1 in range(len(lista_dados)):
        if lista_dados[m1][2] == busca_setor:
            del lista_dados[m1][2]