def melhor_volta(matriz):
    ''''A função recebe uma matriz 6x10 com os tempos em segundos dos 6 corredores em
    cada uma das 10 voltas. A função retorna uma tupla informando: de quem foi a melhor
    volta da prova, com qual tempo e em que volta. Assume-se que os corredores têm tempos
    diferentes.
    list -> tuple''''
    tempo=[]
    for i in range(6):
            list.append(tempo,matriz[i][1])
    menor_tempo=min(tempo)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]==menor_tempo:
                return (i+1,minimo,j+1)