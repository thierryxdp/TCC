def busca(string, matriz):
    '''
    Funcao que recebe uma string representando o setor e uma matriz
    contendo dados dos funcionarios inclusive o setor. A funcao retorna
    uma litacom todos os dados dos funcionarios daquele setor.
    str, list -> list
    '''
    indice_setor = 2
    dados_filtro = []
    for i in range(len(matriz)):
        setor = matriz[i][indice_setor]
        if string == setor:
            dados_filtro.append(matriz[i])

    return dados_filtro