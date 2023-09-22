def busca(setor, matriz):
    '''Funcao que busca os dados dos funcionarios de um determinado setor.
    Recebe como entrada uma matriz contendo em cada linha as informacoes:
    list, str -> list'''

    buscaLista = []

    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            list.append(buscaLista, matriz[i])
        
    return buscaLista