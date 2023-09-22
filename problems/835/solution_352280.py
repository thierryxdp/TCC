def melhor_volta(matriz):
    '''
    	Função que recebe uma matriz onde cada linha corresponde a um corredor e contem 10 colunas com os tempos, em segundos, das voltas.
        A função retorna uma tupla com o corredor da melhor volta, o tempo e qual volta teve o melhor tempo.
        list -> tuple
    '''
    for i in range(len(matriz)):
        'corredor'+ string(i+1) = matriz[i]