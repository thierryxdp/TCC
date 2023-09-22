def melhor_volta(matriz):
    '''Função que recebe um matriz de 6 corredores e 10 voltas e retorna 
    uma tupla contendo o corredor que fez melhor volta, o tempo que feze em que volta
    list(list)-> tuple'''
    for volta in range(0, len(matriz)):
        for tempo in range(0, len(matriz[volta])):
            menorTempo =  min(matriz[volta][tempo], menor_tempo)
            if menor_tempo == matriz[volta][tempo]:
                melhor_tempo = volta + 1
                volta = tempo + 1