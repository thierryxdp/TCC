def busca(setor, matriz):
    '''Função que recebe uma string com o nome do setor da empresa e uma matriz com dados
    de funcionários e retorna os dados de todos os funcionários daquele setor;
    str, list -> list'''
    result = []

    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            result += [[matriz[i][0], matriz[i][1], matriz[i][3]]]

    return result