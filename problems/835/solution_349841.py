def melhor_volta(m):
    '''Retorna o a melhor volta corredor em qual tempo e volta.
    list -> tuple''' 
    corredor = 1
    tempo = m[0][0]
    volta = 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            if min(m[i]) <= tempo and min(m[i]) == m[i][j]:
                tempo = min(m[i])
                volta = j + 1
                corredor = i + 1
    return (corredor, tempo, volta)