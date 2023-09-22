def melhor_volta(matriz):

    menor_tempo = matriz[0][0]
    melhor_corredor = 1
    melhor_volta = 1

    for corredor in range(len(matriz)):
        for volta in range(len(matriz[0])):
            tempo = matriz[corredor][volta]
            if menor_tempo > tempo:
                menor_tempo = tempo
                melhor_corredor = corredor + 1
                melhor_volta = volta + 1


    return  melhor_corredor, menor_tempo, melhor_volta