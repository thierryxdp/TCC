def melhor_volta(m):
    '''Função que recebe uma matriz com os 6 corredores e as 10 voltas
    e retorna uma tupla informando o vencedor e o melhor tempo. list ->
    tuple'''
    result = ()
    for i in range(1, 6):
        for j in range(1, 10):
            result += (min(m[i]), )
        if m[i][j] == min(result):
                x = list.index(m, m[i][j])
    result += (x, min(result), m[i][j])
    return result