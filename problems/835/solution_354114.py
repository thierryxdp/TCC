def melhor_volta(matriz_tempo):
    """
    funcao que retorna uma tupla com a melhor volta, tempo e o numero da volta
    em que ocorreu tal desempenho após o tempo, em segundos, dos corredores por volta ser
    inserido na funcao atraves de uma matriz no formato de lista
    list -> tuple
    """
    best_time = best_volta = best_racer = 1000
    for volta_corredor in range(0, len(matriz_tempo)):
        for tempo_corredor in range(0, len(matriz_tempo[volta_corredor])):
            if min(matriz_tempo[volta_corredor][tempo_corredor], best_time) == matriz_tempo[volta_corredor][tempo_corredor]:
                best_time = min(matriz_tempo[volta_corredor][tempo_corredor], best_time)
                best_racer = volta_corredor + 1
                best_volta = tempo_corredor + 1

    return best_racer, best_time, best_volta