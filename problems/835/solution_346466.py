def melhor_volta(matriz):
    '''Função que retorna o número do corredor com a melhor volta,
    o tempo decorrido e a volta em uma prova de corrida de Kart; list -> tuple'''
    melhor = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < melhor[1]:
                melhor = (i+1,matriz[i][j],j+1)
    return melhor