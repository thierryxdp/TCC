def busca(setor,matriz):
    '''Função que recebe uma string e uma matriz como a do exemplo e faz uma busca
    por setor, ou seja, dado o nome de um setor de empresa,a função retorna uma lista
    com os dados de todos os funcionários daquele setor.
    str,list-->list'''    
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor == matriz[i][j]:
                dados = [[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return dados