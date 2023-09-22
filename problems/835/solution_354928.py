def melhor_volta(matriz):
    '''Retorna quem teve o melhor tempo em uma volta de uma corrida,
    o tempo e em qual volta.
    list -> tuple'''
    indice_corredor = 1
    indice_volta = 1
    melhor_tempo = 99999999999
    
    for corredor in matriz:
        for tempo in corredor:
            if tempo < melhor_tempo:
                melhor_tempo = tempo
                melhor_volta = indice_volta
                melhor_corredor = indice_corredor

            indice_volta = indice_volta + 1

        indice_corredor = indice_corredor + 1
        indice_volta = 1

    return (melhor_corredor, melhor_tempo, melhor_volta)