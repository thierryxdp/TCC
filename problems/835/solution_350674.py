def melhor_volta(matriz):
    '''Função que retirna uma tupla de quem foi a melhor volta da prova, com qual tempo e em que volta.'''
    '''list(list)-> tuple'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(matriz[i][j]):
                volta = len(matriz[i][j])
                corredor = len(matriz[i][j][i])
    tempo = 1
    return (corredor, tempo, volta)