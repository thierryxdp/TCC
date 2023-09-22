def melhor_volta(tempos):
    '''Função que recebe como entrada uma matriz 6 × 10 com os tempos, em
segundos, de corredores de kart em cada volta.'''
    #list -> tuple
    #a tupla informa de quem foi a melhor volta da prova, com qual tempo e em
    #que volta.
    corredor = 0
    menor_tempo = 0
    volta = 0
    for i in range(len(tempos)):
        for j in range(len(tempos[i])):
            if (menor_tempo == 0 or tempos[i][j] < menor_tempo):
                menor_tempo = tempos[i][j]
                corredor = i + 1
                volta = j + 1
    return (corredor, menor_tempo, volta)