def melhor_volta(matriz):
    '''
        Função que recebe uma matriz onde cada linha corresponde a um corredor e contem 10 colunas com os tempos, em segundos, das voltas.
        A função retorna uma tupla com o corredor da melhor volta, o tempo e qual volta teve o melhor tempo.
        list -> tuple
    '''
    melhor_tempo = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < melhor_tempo:
                melhor_tempo = matriz[i][j]
                indice_m_tempo = (i,j)
            melhor_tempo = matriz[i][j]
    
    return (i+1,melhor_tempo,j+1)