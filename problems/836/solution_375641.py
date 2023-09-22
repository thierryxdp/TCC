def busca(setor,matriz):
    '''Funcao que recebe uma matriz e faz uma busca
    por setor, retornando os dados de todos os funcionarios
    daquele setor
    matriz , str -- list> '''
    n=[]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            return [matriz[i][0],matriz[i][1],matriz[i][3]]
        else:
            return []