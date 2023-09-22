def melhor_volta(matriz):
    " " "Recebe como entrada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta, e retorna de quem foi a melhor volta, qual o tempo e em que volta;list, -> tuple " " "
    tempo = []
    volta = []
    corredores = [] 
    for i in range(len(matriz)):
        tempo.append(min(matriz[i]))
        corredores.append(i+1)
        for j in range(len(matriz[i])):
            if matriz[i][j]==min(matriz[i]):
                volta.append(j+1)
    n = list.index(tempo,min(tempo))
    return (corredores[n],min(tempo),volta[n])