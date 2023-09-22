def busca(setor, matriz):
    '''recebe uma matriz(matriz) contendo as informacoes dos funcionarios,
    e o setor(setor) que se deseja buscar, na ordem(setor,matriz),retorna 
    os dados de todos os funcionarios do setor dado; str,list(list) -> list(list)'''
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                dados = dados + [matriz[i][0],matriz[i][1],matriz[i][3]]
    return dados