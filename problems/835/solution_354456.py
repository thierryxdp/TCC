def melhor_volta(m):
    ''' Informa de quem foi a melhor volta da prova, com qual tempo e em que volta, dada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta;
    mat -> tuple '''
    tempomin = [] 
    for l in m:
        tm = min(l)
        list.append(tempomin,tm)
    tempo = min(tempomin)
    corredor = list.index(tempomin,tempo) + 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            if tempo == m[i][j]:
                volta = j + 1
    return (corredor, tempo, volta)