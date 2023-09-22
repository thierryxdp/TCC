def melhor_volta(matriz):
    '''
        Função que recebe uma matriz onde cada linha corresponde a um corredor e contem 10 colunas com os tempos, em segundos, das voltas.
        A função retorna uma tupla com o corredor da melhor volta, o tempo e qual volta teve o melhor tempo.
        list -> tuple
    '''
    melhor_tempo = matriz[0][0]
    corredor = 0
    volta=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < melhor_tempo:
                melhor_tempo = matriz[i][j]
                corredor = i
                volta = j
    
    return ((corredor) +1,melhor_tempo,(volta)+1)
        
    
    return (corredor+1,menor_tempo,volta+1)