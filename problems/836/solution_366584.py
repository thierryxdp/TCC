def busca(string, matriz):
    '''recebe uma string referente ao setor da empresa e uma matriz que
    armazena os dados dos funcionários dessa empresa, retorna os dados de
    todos os funcionários da empresa
    string, list ->list'''
    retorna =[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if string ==matriz[i][j]:
                retorna.append(matriz[i])
                retorna.remove(string)
    return retorna