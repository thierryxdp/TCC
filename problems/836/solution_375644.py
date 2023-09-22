def busca(setor,matriz):
    '''Funcao que recebe uma matriz e faz uma busca
    por setor, retornando os dados de todos os funcionarios
    daquele setor
    matriz , str -- list> '''
    n=[]
    for n in range(len(matriz)):
        if matriz[n][2] == setor:
            return [matriz[n][0],matriz[n][1],matriz[n][3]],[matriz[2][0], matriz[2][1], matriz[2][3]]
        else:
            return []