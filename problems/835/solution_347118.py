def melhor_volta(corrida):
    '''Analisa qual foi a melhor volta de uma corrida
list -> (int, float, int)'''
    corredor = 0
    volta = 0
    tempo = corrida[0][0]
    for i in range(len(corrida)):
        for j in range(len(corrida[i])):
            if corrida[i][j] < tempo:
                corredor = i
                volta = j
                tempo = corrida[i][j]
    return (corredor+1, tempo, volta+1)