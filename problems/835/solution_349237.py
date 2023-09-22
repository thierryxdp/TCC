def melhor_volta(corrida):
    corredor = 0
    volta = 0
    tempo = corrida[0][0]
    for i in range(len(corrida)):
        if min(corrida[i]) < tempo:
            tempo = min(corrida[i])
            for j in range(len(corrida[i])):
                if corrida[i][j] == min(corrida[i])
                corredor = i
                volta = j
    
    return (corredor+1, tempo, volta+1)