def melhor_volta(tempos):
    '''Recebe uma matriz 6x10 com os tempos dos corredores em cada volta.
    Retorna uma tupla informando: De quem foi a melhor volta da prova, com qual tempo e em que volta;
    list -> tup (int, int, int)'''

    piloto = 0
    volta = 0
    menor_tempo = tempos[0][0]

    for i in range(len(tempos)):
        for j in range(len(tempos[i])):
            if tempos[i][j] < menor_tempo:
                piloto = i + 1
                volta = j + 1
                menor_tempo = tempos[i][j]

    return (piloto, menor_tempo, volta)