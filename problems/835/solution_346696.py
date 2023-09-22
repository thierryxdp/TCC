def melhor_volta(m):
    '''Função que recebe uma matriz com os 6 corredores e as 10 voltas
    e retorna uma tupla informando o vencedor e o melhor tempo. list ->
    tuple'''
    from math import *
    result = ()
    for i in range(len(m)):
        for j in range(0, 10):
            if m[i][j] == min(m[i]):
                result += (m[i][j])
        result += (list.index(m, m[i]), min(result))
    return result