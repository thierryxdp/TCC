def busca(string, matriz):
    '''recebe uma string referente ao setor da empresa e uma matriz que 
    armazena os dados dos funcionários dessa empresa, retorna os dados de
    todos os funcionários da empresa
    str, list ->list'''
    retorna =[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if string == matriz[i][j]:
                list.append(retorna, matriz[i][0]+matriz[i][1])
    return retorna